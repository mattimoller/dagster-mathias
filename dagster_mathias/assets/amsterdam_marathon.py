import requests
from dagster import asset

from utils import env
from utils.slack import send_slack_message


def get_bib_status() -> dict:
    # Define the URL of the GraphQL API
    url = "https://atleta.cc/api/graphql"

    headers = {
        "Content-Type": "application/json",
    }

    # Define the GraphQL query payload
    payload = {
        "operationName": "GetRegistrationsForSale",
        "variables": {"id": "nhIVueqEDrvO", "tickets": None, "limit": 10},
        "query": """
      query GetRegistrationsForSale($id: ID!, $tickets: [String!], $limit: Int!) {
        event(id: $id) {
          id
          registrations_for_sale_count
          filtered_registrations_for_sale_count: registrations_for_sale_count(
            tickets: $tickets
          )
          sold_registrations_count
          tickets_for_resale {
            id
            title
            __typename
          }
          registrations_for_sale(tickets: $tickets, limit: $limit) {
            id
            ticket {
              id
              title
              __typename
            }
            time_slot {
              id
              start_date
              start_time
              title
              multi_date
              __typename
            }
            promotion {
              id
              title
              __typename
            }
            upgrades {
              id
              product {
                id
                title
                is_ticket_fee
                __typename
              }
              product_variant {
                id
                title
                __typename
              }
              __typename
            }
            resale {
              id
              available
              total_amount
              fee
              public_url
              public_token
              __typename
            }
            __typename
          }
          __typename
        }
      }
      """,
    }

    # Send the request to the API
    response = requests.post(url, headers=headers, json=payload)

    # Check if the response was successful
    if response.status_code == 200:
        print("Response received successfully!")
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)
        raise ValueError("Failed to retrieve data")


def check_num_bibs_available(data: dict) -> tuple[int, int]:
    return (
        data["data"]["event"]["registrations_for_sale_count"],
        data["data"]["event"]["filtered_registrations_for_sale_count"],
    )


@asset()
def bib_reporter() -> None:
    data = get_bib_status()
    num_bibs_available, filtered_bibs_available = check_num_bibs_available(data)

    if num_bibs_available == 0:
        print("There are no bibs available")
        return
    text = f"There are {num_bibs_available} bibs available, {filtered_bibs_available} filtered bibs available! :athletic_shoe: <https://www.tcsamsterdammarathon.eu/bib-number-supply-demand|Webpage>"
    payload = {"text": text}

    send_slack_message(payload, env.get_env_var("SLACK_WEBHOOK_URL"))
