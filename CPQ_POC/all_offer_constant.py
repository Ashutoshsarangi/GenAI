
get_product_offering_url = 'https://amd-apigw-stack-service-cmm-cpq-oc-2505-v1-rt.apps.ilocpcpq419.ocpd.corp.amdocs.com/productOfferingDiscovery/v1.1/productOffering?customerType=M&mustBeBundled=false&categoryName=Packages,Standalone&disablePreSearchProductOfferingHook=false&checkQualification=true&offset=0&limit=50'

create_digital_template_url = 'https://amd-apigw-stack-service-eu-cmm-cpq-tigers-8-rt.apps.ilocpcpq413.ocpd.corp.amdocs.com/c1tosqoentitymanagement-ms/c1toSqoEntityManagement/v1/framework-agreements/IFrameworkAgreement_575/product-offering-agreement-items/create-digital-template?customerId=700000282&salesChannel=SA'

headers = {
    'Authorization': '',
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US",
    "Content-Type": "application/json",
    "Origin": "http://localhost:4002",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

product_offers = [
  {
    'id': '879f90d8-4cff-4951-8619-927611c01178',
    'name': 'Coax Underlay Connectivity'
  },
  {
    'id': 'ddcf1da4-782d-479e-8455-7f9359c70385',
    'name': 'Ethernet Switch Equipment'
  },
  {
    'id': 'bd099f28-b2a0-4629-aaf4-0e4bfd3475a2',
    'name': 'Data and Voice Equipment (Rental)'
  },
  { 'id': '82823e76-9ecb-4a66-bc7d-0edc9610a601', 'name': 'SASE Gateway' },
  {
    'id': 'e1663f14-261a-488a-b49d-1dfe84d8f70c',
    'name': 'SD-WAN Fortinet'
  },
  {
    'id': 'e8888545-bbe5-4a78-948a-585aa48cca04',
    'name': 'SD-WAN High Availability Add-On'
  },
  {
    'id': 'dbaa0487-ddaf-47e7-bc6c-5c1749eb041b',
    'name': 'Business Voice'
  },
  { 'id': '798d8dce-e9ce-4f15-bf8f-0fb61477d6a6', 'name': 'SD-WAN' },
  {
    'id': 'ad22118e-7c37-4925-b1ff-e4d746bf0a63',
    'name': 'UTM Fortinet High Availability Add-on'
  },
  { 'id': 'c0349c14-a450-4d3f-b0c9-998faa9121f1', 'name': 'Site Access' },
  {
    'id': '6399b99a-262c-4194-b8a2-9b05a840d288',
    'name': 'SD-WAN SASE High Availability Add-On'
  },
  {
    'id': 'dceeaef9-645f-4187-b9a2-c4c5be5cb798',
    'name': 'SD-WAN Fortinet High Availability Add-on'
  },
  { 'id': 'd4f5742c-e8c1-4581-a30a-3c9b9c38d26a', 'name': 'PRI' },
  {
    'id': '7f998753-1553-4257-a958-44876b690985',
    'name': 'PRI Professional Installation'
  },
  {
    'id': '9d8eee62-75a5-4c73-b6cb-f8dd76d5c2b4',
    'name': 'SIP Professional Installation'
  },
  { 'id': '78aaae07-e584-4460-b791-cebf4952723f', 'name': 'SD-WAN SASE' },
  {
    'id': '49fa4bff-5cc6-4b57-a150-ede28cf419a4',
    'name': 'Managed Wireless LAN'
  },
  {
    'id': '4251c35b-1e40-4674-9943-80783e0b2382',
    'name': 'Business Internet'
  },
  {
    'id': '83c36493-bfad-46b7-aab5-0537ca50b329',
    'name': 'DDoS Mitigation'
  },
  { 'id': '62d1a0a1-d006-448c-962f-676c4da23caa', 'name': 'uCPE' },
  {
    'id': 'e7293100-3498-41b7-83e6-2603cac75608',
    'name': 'Wireless Backup'
  },
  {
    'id': '0e669758-1d74-4365-be96-c5e2b264aec4',
    'name': 'Managed Wireless LAN Fortinet'
  },
  { 'id': '99f2f37b-73e1-4561-8a48-59a4e70a7994', 'name': 'UTM Fortinet' },
  {
    'id': '3170eacb-6c50-45f7-b400-4c4ccae9197b',
    'name': 'Managed Detection and Response (MDR)'
  },
  {
    'id': '2134e594-73d4-4f99-9ace-93deff7ad0ae',
    'name': 'Hardware Router'
  },
  {
    'id': 'fc73100f-b7d8-49f4-b772-9a63b0402d97',
    'name': 'OIA Professional Installation'
  },
  {
    'id': '65912395-2d46-4953-a16e-f378e5a57763',
    'name': 'Dedicated Internet'
  },
  {
    'id': 'b472cda2-c91d-4ce2-b9f8-2af232f8bd16',
    'name': 'Fiber Underlay Connectivity'
  },
  {
    'id': '267778aa-ddbb-49a9-a477-cbe35766cc0b',
    'name': 'Hardware Managed Router'
  },
  {
    'id': 'fb572bd1-04a3-44a9-9ae3-16e26ad0b1cd',
    'name': 'SD-WAN Cloud Connect High Availability Add-on'
  },
  { 'id': '2b4908fd-d2fa-42da-80f0-9bc29c373db7', 'name': 'SIP' },
  {
    'id': 'caebbdfe-f783-4fe0-ace0-8e74b12a26f7',
    'name': 'Endpoint Detection & Response (EDR)'
  },
  {
    'id': '563e0606-7739-49f4-81ea-0db18fca099c',
    'name': 'SD-WAN Cloud Connect'
  },
  {
    'id': '45cc81a4-54fa-454c-adb8-14fec9cad8ee',
    'name': 'Ethernet Dedicated Internet'
  },
  {
    'id': '3772dc84-bf45-40c8-9554-37f1d542aba1',
    'name': 'Hardware Router Professional Installation'
  },
  {
    'id': '9fddfff1-7f76-4572-818f-67c510602db5',
    'name': 'Managed Connectivity'
  }
]
