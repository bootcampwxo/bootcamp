import pandas as pd

# Data
all_po_data = [
    {
        "pom_id": "4697",
        "po_number": "4300016793",
        "submitted_by": "Sailendu Patra",
        "user_id": "sailendu.patra"
    },
    {
        "pom_id": "3426",
        "po_number": "4200054529",
        "submitted_by": "Tannavi Snehal",
        "user_id": "tannavi.snehal"
    },
    {
        "pom_id": "1847",
        "po_number": "4100096723",
        "submitted_by": "Shivam Patel",
        "user_id": "shivam.patel"
    },
    {
        "pom_id": "2059",
        "po_number": "4900048319",
        "submitted_by": "Harshil Turakhia",
        "user_id": "harshil.turakhia"
    }
]

po_data = [
    {
        "po_date": "23-12-2023",
        "po_number": "4300016793",
        "payment_terms": "A012",
        "quote_number": "23MS2022002018",
        "bill_to_party_name": "AMBA RIVER COKE LTD. _TOP_1",
        "bill_to_party_address": "Geetapuram, Village Dolvi, Tai-Pen Raigad, Dolvi -402107, State Maharashtra",
        "bill_to_party_gstin": "27AAACG5394G1ZH",
        "ship_to_party_name": "AMBA RIVER COKE LTD. _TOP_1",
        "ship_to_party_address": "Geetapuram, Village Dolvi, Tai - PenRaigad, Dolvi-402107, State Maharashtra",
        "ship_to_party_gstin": "27AAACG5394G1ZH",
        "product_desc": "SVC.SEAFRT JSW ARJUNGAD",
        "qty": "7,872.000",
        "unit_rate": "430.35",
        "taxable_value": "3,387,715.20",
        "total_amount": "3,997,503.00"
    }
]

quotation_data = [{   
        "quotation_number": "23MS2022002018",
        "payment_terms": "A012",
        "bill_to_party_name": "AMBA RIVER COKE LTD. _TOP_1",
        "bill_to_party_address": "Geetapuram, Village Dolvi, Tai-Pen Raigad, Dolvi -402107, State Maharashtra",
        "bill_to_party_gstin": "27AAACG5394G1ZH",
        "ship_to_party_name": "AMBA RIVER COKE LTD. _TOP_1",
        "ship_to_party_address": "Geetapuram, Village Dolvi, Tai - PenRaigad, Dolvi-402107, State Maharashtra",
        "ship_to_party_gstin": "27AAACG5394G1ZH",
        "product_desc": "SVC.SEAFRT JSW ARJUNGAD",
        "qty": "7,872.000",
        "unit_rate": "430.35",
        "taxable_value": "3,387,715.20",
        "total_amount": "3,997,503.00"
    
}
]

all_remittance_data = [
    {
        "remittance_id": "34539215",
        "payer_name": "AMBA RIVER COKE LTD. _TOP_1",
        "payee_name": "JSW Logistics & Shipping Ltd.",
        "payment_date": "23-12-2024",
        "payment_method": "Cheque"
    },
    {
        "remittance_id": "39750740",
        "payer_name": "Tata Steel Ltd.",
        "payee_name": "XYZ Logistics Pvt. Ltd.",
        "payment_date": "10-01-2025",
        "payment_method": "Bank Transfer"
    },
    {
        "remittance_id": "893740194",
        "payer_name": "Reliance Industries Ltd.",
        "payee_name": "Oceanic Shipping Services",
        "payment_date": "05-02-2025",
        "payment_method": "Online Payment"
    },
    {
        "remittance_id": "947593948",
        "payer_name": "Larsen & Toubro Ltd.",
        "payee_name": "Global Freight Movers",
        "payment_date": "15-01-2025",
        "payment_method": "Wire Transfer"
    },
    {
        "remittance_id": "018375849",
        "payer_name": "Hindalco Industries Ltd.",
        "payee_name": "Seaway Transporters Ltd.",
        "payment_date": "08-02-2025",
        "payment_method": "Credit Card"
    }
]



remittance_data = [{
    "remittance_id":"34539215",
    "invoice_number":"3189",
    "invoice_amount":"393.60",
    "payment_date":"5 July 2013"
}]

invoice_data = [{
    "invoice_number":"3189",
    "invoice_amount":"393.60"
}]

order_data = [{
    "order_id":"716484927",
    "order_date":"25-01-2025",
    "order_update":"Order is delayed as the ordered quantity is not available in the current inventory. Updated delivery date is 31-01-2025"
},
    {
    "order_id":"716000927",
    "order_date":"15-01-2025",
    "order_update":"Order is shipped. Updated delivery date is 21-01-2025"
    }
              ]

user_emails = [
    {"name": "Acme Corp - John Smith", "email": "john.smith@acmecorp.com"},
    {"name": "Globex Ltd - Maria Gonzales", "email": "maria.gonzales@globex.com"},
    {"name": "Initech Solutions - Raj Mehta", "email": "raj.mehta@initech.com"},
    {"name": "Umbrella Inc - Lily Tran", "email": "lily.tran@umbrella.com"},
    {"name": "Wayne Enterprises - Bruce Wayne", "email": "bruce.wayne@wayneenterprises.com"}
]

# Convert to DataFrames
all_po_data_df = pd.DataFrame(all_po_data)
po_data_df = pd.DataFrame(po_data)
quotation_data_df = pd.DataFrame(quotation_data)
all_remittance_df = pd.DataFrame(all_remittance_data)
remittance_data_df = pd.DataFrame(remittance_data)
invoice_data_df = pd.DataFrame(invoice_data)
order_data_df = pd.DataFrame(order_data)
user_emails_df = pd.DataFrame(user_emails)


selected_columns = ["payment_terms",
        "bill_to_party_name",
        "bill_to_party_address",
        "bill_to_party_gstin",
        "ship_to_party_name",
        "ship_to_party_address",
        "ship_to_party_gstin",
        "product_desc",
        "qty",
        "unit_rate",
        "taxable_value",
        "total_amount"]

po_selected_df = po_data_df[selected_columns]

# Select only required columns from Quotation Data
quotation_selected_df = quotation_data_df[selected_columns]

# Create a DataFrame for comparison
po_comparison_data = []

# Iterate over selected columns and compare values
for column in selected_columns:
    po_value = po_selected_df[column].values[0] if column in po_selected_df else None
    quotation_value = quotation_selected_df[column].values[0] if column in quotation_selected_df else None
    match_result = "Match" if po_value == quotation_value else "Mismatch"

    po_comparison_data.append({
        "entity_name": column,
        "po_details": po_value,
        "quotation_details": quotation_value,
        "matching_result": match_result
    })

po_comparison_df = pd.DataFrame(po_comparison_data)

selected_columns = ["invoice_number", "invoice_amount"]

remittance_selected_df = remittance_data_df[selected_columns]
invoice_selected_df = invoice_data_df[selected_columns]

# Prepare comparison data
inv_comparison_data = []

for column in selected_columns:
    remittance_value = remittance_selected_df[column].values[0] if column in remittance_selected_df else None
    invoice_value = invoice_selected_df[column].values[0] if column in invoice_selected_df else None
    match_result = "Match" if po_value == quotation_value else "Mismatch"

    inv_comparison_data.append({
        "entity_name":column,
        "remittance_data": remittance_value,
        "invoice_data": invoice_value,
        "matching_result": match_result
    })

# Convert to DataFrame for better visualization
inv_comparison_df = pd.DataFrame(inv_comparison_data)


