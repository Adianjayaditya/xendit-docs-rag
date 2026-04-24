---
url: https://docs.xendit.co/apidocs/create-payment-request
title: "Create a payment request"
section: apidocs
product: xendit
---

# Create a payment request

## Endpoint
`POST /v3/payment_requests`

Create payment request. Initiates payment collection from end user.

## Header Parameters

- **api-version** (string)
- **for-user-id** (string): The XenPlatform subaccount user id that will perform this transaction.
- **with-split-rule** (string): The XenPlatform split rule id that will be applied to this transaction.

## Body Parameters

- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): PAY: Create a payment request that is able to receive one payment. [Valid values[ "PAY" ]]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, required): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **customer_id** (string, optional): Xendit unique Capture ID generated as reference for the end user [Max length41]
- **type** (string, required): Type of customer [Valid values[ "INDIVIDUAL" ]]
- **reference_id** (string, required): Merchant provided identifier for the customer. Must be unique. Alphanumeric no special characters allowed [Min length1]
- **email** (string  (email), optional): E-mail address of customer. Maximum length 50 characters [Min length4]
- **mobile_number** (string, optional): Mobile number of customer in E.164 format +(country code)(subscriber number) [Min length1]
- **given_names** (string, required): Primary or first name/s of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **surname** (string, optional): Last or family name of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **nationality** (string, optional): Country code for customer nationality. ISO 3166-1 alpha-2 Country Code [Min length2]
- **place_of_birth** (string, optional): City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed. [Min length1]
- **date_of_birth** (string, optional): Date of birth of the customer. Format: YYYY-MM-DD [Min length10]
- **gender** (, optional): Gender of customer [Valid values[ "MALE", "FEMALE", "OTHER" ]]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]
- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): PAY_AND_SAVE: Create a payment request that is able to receive one payment. If the payment is successful, a reusable payment token will be returned in the callback as saved payment information for subsequent payment requests. [Valid values[ "PAY_AND_SAVE" ]]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, required): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **customer_id** (string, optional): Xendit unique Capture ID generated as reference for the end user [Max length41]
- **type** (string, required): Type of customer [Valid values[ "INDIVIDUAL" ]]
- **reference_id** (string, required): Merchant provided identifier for the customer. Must be unique. Alphanumeric no special characters allowed [Min length1]
- **email** (string  (email), optional): E-mail address of customer. Maximum length 50 characters [Min length4]
- **mobile_number** (string, optional): Mobile number of customer in E.164 format +(country code)(subscriber number) [Min length1]
- **given_names** (string, required): Primary or first name/s of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **surname** (string, optional): Last or family name of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **nationality** (string, optional): Country code for customer nationality. ISO 3166-1 alpha-2 Country Code [Min length2]
- **place_of_birth** (string, optional): City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed. [Min length1]
- **date_of_birth** (string, optional): Date of birth of the customer. Format: YYYY-MM-DD [Min length10]
- **gender** (, optional): Gender of customer [Valid values[ "MALE", "FEMALE", "OTHER" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]
- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): PAY: Create a payment request that is able to receive one payment. [Valid values[ "PAY" ]]
- **payment_token_id** (string, required): Xendit unique Payment Token ID generated as reference for reusable payment details of the end user. [Examplept-cc3938dc-c2a5-43c4-89d7-7570793348c2]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, required): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **customer_id** (string, optional): Xendit unique Capture ID generated as reference for the end user [Max length41]
- **type** (string, required): Type of customer [Valid values[ "INDIVIDUAL" ]]
- **reference_id** (string, required): Merchant provided identifier for the customer. Must be unique. Alphanumeric no special characters allowed [Min length1]
- **email** (string  (email), optional): E-mail address of customer. Maximum length 50 characters [Min length4]
- **mobile_number** (string, optional): Mobile number of customer in E.164 format +(country code)(subscriber number) [Min length1]
- **given_names** (string, required): Primary or first name/s of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **surname** (string, optional): Last or family name of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **nationality** (string, optional): Country code for customer nationality. ISO 3166-1 alpha-2 Country Code [Min length2]
- **place_of_birth** (string, optional): City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed. [Min length1]
- **date_of_birth** (string, optional): Date of birth of the customer. Format: YYYY-MM-DD [Min length10]
- **gender** (, optional): Gender of customer [Valid values[ "MALE", "FEMALE", "OTHER" ]]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]
- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): REUSABLE_PAYMENT_CODE: Create one payment request that is able to receive multiple payments. This is only used for repeat use payment method like static QR, static OTC payment code or a predefined Virtual Account number. [Valid values[ "REUSABLE_PAYMENT_CODE" ]]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, optional): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]

## Response Codes

- **201**
- **400**
- **403**
- **409**
- **500**
- **503**

## Response Body

- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): PAY: Create a payment request that is able to receive one payment. [Valid values[ "PAY" ]]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, required): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **customer_id** (string, optional): Xendit unique Capture ID generated as reference for the end user [Max length41]
- **type** (string, required): Type of customer [Valid values[ "INDIVIDUAL" ]]
- **reference_id** (string, required): Merchant provided identifier for the customer. Must be unique. Alphanumeric no special characters allowed [Min length1]
- **email** (string  (email), optional): E-mail address of customer. Maximum length 50 characters [Min length4]
- **mobile_number** (string, optional): Mobile number of customer in E.164 format +(country code)(subscriber number) [Min length1]
- **given_names** (string, required): Primary or first name/s of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **surname** (string, optional): Last or family name of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **nationality** (string, optional): Country code for customer nationality. ISO 3166-1 alpha-2 Country Code [Min length2]
- **place_of_birth** (string, optional): City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed. [Min length1]
- **date_of_birth** (string, optional): Date of birth of the customer. Format: YYYY-MM-DD [Min length10]
- **gender** (, optional): Gender of customer [Valid values[ "MALE", "FEMALE", "OTHER" ]]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]
- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): PAY_AND_SAVE: Create a payment request that is able to receive one payment. If the payment is successful, a reusable payment token will be returned in the callback as saved payment information for subsequent payment requests. [Valid values[ "PAY_AND_SAVE" ]]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, required): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **customer_id** (string, optional): Xendit unique Capture ID generated as reference for the end user [Max length41]
- **type** (string, required): Type of customer [Valid values[ "INDIVIDUAL" ]]
- **reference_id** (string, required): Merchant provided identifier for the customer. Must be unique. Alphanumeric no special characters allowed [Min length1]
- **email** (string  (email), optional): E-mail address of customer. Maximum length 50 characters [Min length4]
- **mobile_number** (string, optional): Mobile number of customer in E.164 format +(country code)(subscriber number) [Min length1]
- **given_names** (string, required): Primary or first name/s of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **surname** (string, optional): Last or family name of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **nationality** (string, optional): Country code for customer nationality. ISO 3166-1 alpha-2 Country Code [Min length2]
- **place_of_birth** (string, optional): City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed. [Min length1]
- **date_of_birth** (string, optional): Date of birth of the customer. Format: YYYY-MM-DD [Min length10]
- **gender** (, optional): Gender of customer [Valid values[ "MALE", "FEMALE", "OTHER" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]
- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): PAY: Create a payment request that is able to receive one payment. [Valid values[ "PAY" ]]
- **payment_token_id** (string, required): Xendit unique Payment Token ID generated as reference for reusable payment details of the end user. [Examplept-cc3938dc-c2a5-43c4-89d7-7570793348c2]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, required): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **customer_id** (string, optional): Xendit unique Capture ID generated as reference for the end user [Max length41]
- **type** (string, required): Type of customer [Valid values[ "INDIVIDUAL" ]]
- **reference_id** (string, required): Merchant provided identifier for the customer. Must be unique. Alphanumeric no special characters allowed [Min length1]
- **email** (string  (email), optional): E-mail address of customer. Maximum length 50 characters [Min length4]
- **mobile_number** (string, optional): Mobile number of customer in E.164 format +(country code)(subscriber number) [Min length1]
- **given_names** (string, required): Primary or first name/s of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **surname** (string, optional): Last or family name of customer. Alphanumeric. No special characters is allowed. [Min length1]
- **nationality** (string, optional): Country code for customer nationality. ISO 3166-1 alpha-2 Country Code [Min length2]
- **place_of_birth** (string, optional): City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed. [Min length1]
- **date_of_birth** (string, optional): Date of birth of the customer. Format: YYYY-MM-DD [Min length10]
- **gender** (, optional): Gender of customer [Valid values[ "MALE", "FEMALE", "OTHER" ]]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]
- **reference_id** (string, required): A reference ID from merchants to identify their request. For "CARDS" channel code, reference ID must be unique. [Min length1]
- **type** (string, required): REUSABLE_PAYMENT_CODE: Create one payment request that is able to receive multiple payments. This is only used for repeat use payment method like static QR, static OTC payment code or a predefined Virtual Account number. [Valid values[ "REUSABLE_PAYMENT_CODE" ]]
- **country** (string, required): ISO 3166-1 alpha-2 two-letter country code for the country of transaction. [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "HK", "MX" ]]
- **currency** (string, required): ISO 4217 three-letter currency code for the payment. [Valid values[ "IDR", "PHP", "VND", "THB", "SGD", "MYR", "USD", "HKD", "AUD", "GBP", "EUR", "JPY", "MXN" ]]
- **channel_code** (string, required): Channel code used to select the payment method provider.
- **request_amount** (number, optional): The intended payment amount to be collected from the end user. [Minimum0.0]
- **capture_method** (string, optional): AUTOMATIC: payment capture will be processed immediately after payment request is created.
MANUAL: payment capture requires merchant's trigger via payment capture endpoint before being processed [Valid values[ "AUTOMATIC", "MANUAL" ]]
- **description** (string, optional): A custom description for the Payment Request. [Min length1]
- **reference_id** (string, required): Merchant provided identifier for the item [Min length1]
- **type** (, optional): Type of item [Valid values[ "DIGITAL_PRODUCT", "PHYSICAL_PRODUCT", "DIGITAL_SERVICE", "PHYSICAL_SERVICE", "FEE" ]]
- **name** (string, required): Name of item [Min length1]
- **net_unit_amount** (number, required): Net amount to be charged per unit
- **quantity** (integer, required): Number of units of this item in the basket [Minimum1.0]
- **url** (string, optional): URL of the item. Must be HTTPS or HTTP
- **image_url** (string, optional): URL of the image of the item. Must be HTTPS or HTTP
- **category** (string, required): Category for item [Max length255]
- **subcategory** (string, optional): Sub-category for item [Max length255]
- **description** (string, optional): Description of item [Max length255]
- **country** (, optional): 2-letter ISO 3166-2 country code for the customer’s shipping country [Valid values[ "ID", "PH", "VN", "TH", "SG", "MY", "MX" ]]
- **street_line1** (string, optional): Building name and apartment unit number [Min length1]
- **street_line2** (string, optional): Building street address [Min length1]
- **city** (string, optional): City, village or town as appropriate [Min length1]
- **province_state** (string, optional): Either one of (whichever is applicable): Geographic area, province, or region / Formal state designation within country [Min length1]
- **postal_code** (string, optional): Postal, zip or rural delivery code, if applicable [Min length1]
