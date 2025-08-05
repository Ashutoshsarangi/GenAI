import requests
import json
import random
from all_offer_constant import product_offers
from langchain_core.tools import tool

@tool
def get_product_offers(product_offer_names: list):
    '''Extracts product offers based on the provided names. and return result dict 
    which will contain productOfferingInstance which will again contain c1RootOfferId and productOfferingName
    [
        {
            "productOfferingInstance": {
                "c1RootOfferId": "d4f5742c-e8c1-4581-a30a-3c9b9c38d26a",
                "productOfferingName": "PRI"
            }
        },
        {
            "productOfferingInstance": {
                "c1RootOfferId": "08501022-6107-4063-8ca3-28f58924ec86",
                "productOfferingName": "Dedicated Internet"
            }
        }
    ]
    '''
    result = []
    product_offer_names = [offer.lower() for offer in product_offer_names]
    for product in product_offers:
        if (product['name'].lower() in product_offer_names):
            result.append({
                "productOfferingInstance": {
                    "c1RootOfferId": product['id'],
                    "productOfferingName": product['name'],
                }
            })
    print('Product offers found:', result)
    return result

@tool
def create_digital_template_prepare_payload(payload:list):
    '''Creates a digital template payload with the provided productOfferingInstance. 
    Which is a list of product offers from get_product_offers tool. and update template_payload from graph state'''

    payload = {
        "id": "",
        "productOfferingAgreementItem": payload,
        "productInventoryItem": [],
        "name": "Template 02" #+ str(random.randint(10, 100)),
    }
    print('Payload created:', json.dumps(payload, indent=2))
    return payload;

@tool
def multiply(a, b):
    '''a * b'''

    return a*b

@tool
def add(a, b):
    '''a + b'''

    return a + b

@tool
def divide(a, b):
    '''a / b'''
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    
    return a / b

if __name__ == '__main__':
    product_offer_names = [
        'Business Internet',
        'SD-WAN',
        'Business Voice',
        'SIP',
        'PRI'
    ]
    result = get_product_offers(["Business Internet", "SD-WAN", "Business Voice"])
    print(result)
         