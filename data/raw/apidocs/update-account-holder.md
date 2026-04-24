---
url: https://docs.xendit.co/apidocs/update-account-holder
title: "Update account holder"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [xenPlatform](/apidocs/accounts-misc-introduction)
  - [xenPlatform](/apidocs/create-account)

What information are you looking for?

Overview

Use ↑/↓ to navigate

[Quick setup](/apidocs/quick-setup)

[Rate limits](/apidocs/rate-limits)

[Webhook behavior](/apidocs/webhook-behavior)

Payments

Download API reference

[Introduction](/apidocs/introduction)

Payment Request

Payment

Payment Token

Session

Refund

Subscriptions

[Payment Link](/apidocs/payment-link)

[BI SNAP](/apidocs/bi-snap)

Payouts

Download API reference

[Introduction](/apidocs/payouts-introduction)

Payout

Cross-Border Payout

Balance & Transactions

Download API reference

[Introduction](/apidocs/introduction-1)

Balance

Reports

Transaction

xenPlatform

Download API reference

[Introduction](/apidocs/accounts-misc-introduction)

xenPlatform

post

 [Create account](/apidocs/create-account)

get

 [List accounts](/apidocs/list-accounts)

get

 [Get account](/apidocs/get-account)

pat

 [Update account](/apidocs/update-account)

post

 [Create split rule](/apidocs/create-split-rule)

post

 [Create account holder](/apidocs/create-account-holder)

get

 [Get account holder](/apidocs/get-account-holder)

pat

 [Update account holder](/apidocs/update-account-holder)

get

 [Get transfer by reference](/apidocs/get-transfer-by-reference)

post

 [Create transfers](/apidocs/create-transfers)

post

 [Owned account status webhook notification](/apidocs/owned-account-status-webhook-notification)

post

 [Managed account status webhook notification](/apidocs/managed-account-status-webhook-notification)

post

 [Account suspension webhook notification](/apidocs/account-suspension-webhook-notification)

post

 [Account holder KYC status notification webhook](/apidocs/account-holder-kyc-status-notification-webhook)

post

 [Account holder capabilities notification webhook](/apidocs/account-holder-capabilities-notification-webhook)

post

 [Split payment status notification webhook](/apidocs/split-payment-status-notification-webhook)

Webhook Settings

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

Bill Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Update account holder

- Updated on Jan 8, 2026
- Published on Dec 6, 2024

 [Prev](/apidocs/get-account-holder "Get account holder")  [Next](/apidocs/get-transfer-by-reference "Get transfer by reference") 

Patch

/account\_holders/{id}

Use the Update Account Holder endpoint to:

1. Update your Account Holder information. This step may be needed when the your information and document submission is insufficient or invalid (e.g invalid website, blurry selfie, invalid ID, etc.).
2. Activate a payment channel Capability on an Account Holder object associated with a sub-account

You need to provide an URL to receive webhooks. Please specify your URL in [Webhook Settings](https://dashboard.xendit.co/settings/developers#callbacks) in the Xendit Dashboard.

> You will need the Account Holder `Write` API key permission to perform this request.

Security

HTTP

Type basic

Path parameters

id

stringRequired

Example4376b7b0-1c44-46be-8640-828f79cdc8be

Body parameters

Show example

application/json

Update Website
Update KYC Document
Activate Payment Channel Capabilities

Update Website

Code snippet

```
{
  "website_url": "valid-marketplace.brand.com"
}
```

JSON

Copy

Update KYC Document

Code snippet

```
{
  "kyc_documents": [
    {
      "country": "PH",
      "type": "LATEST_GIS_DOCUMENT",
      "file_id": "63f8719642f5856dc9feje7"
    }
  ]
}
```

JSON

Copy

Activate Payment Channel Capabilities

Code snippet

```
{
  "capabilities": [
    {
      "type": "MONEY_IN",
      "channel_code": "PH_CARDS"
    },
    {
      "type": "MONEY_IN",
      "channel_code": "GCASH"
    }
  ]
}
```

JSON

Copy

Collapse all

object

business\_detail

object (business\_detail)

An object containing the business detail of the Account Holder

type

string

The entity type of the business

Valid values[
"CORPORATION",
"PARTNERSHIP",
"SOLE\_PROPRIETORSHIP",
"INDIVIDUAL",
"FOREIGN",
"FOREIGN\_SEC",
"FOREIGN\_NONSEC"
]

legal\_name

string

Legal name of the business. This must match the documentation submitted.

trading\_name

string

Trading or brand name of the business. This will be the name that appears to endpayer on payment page.

description

string

Description of the business. Please specify what business model or goods and services that the business provide. Max 1000 characters.

industry\_category

string

One of our accepted Industry Category Codes depending on your entity type and country of operation.

Refer to the list of [accepted industry category codes here](https://docs.xendit.co/docs/create-verification-requests#list-of-accepted-industry-categories)

date\_of\_registration

string (date)

Business registration date in YYYY-MM-DD

country\_of\_operation

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

individual\_details

Array of object (individual\_detail)

object

An object containing the individual details of the Account Holder. This could be the details of the business owner, director etc.

type

string Required

At least one individual with the type `PIC` (Person in Charge) is required. You may submit multiple PICs for your business in this object.
A minimum 1 Incorporator and 1 PIC is required when they need to activate Cards capabilities.

Valid values[
"PIC",
"Incorporator"
]

role

string Required

This role specifies the role of the PIC or Incorporator. E.g. Owner, Director, Administrator.

given\_names

string Required

First and middle name (if any) of the account holder

Max length255

surname

string Required

Surname or family name of the account holder

Max length255

phone\_number

string Required

The contact number of the Account Holder in `E.164` format. This may also be a landline.

Max length30

email

string Required

The email address of the account holder

Max length255

nationality

string Required

Country code for customer's nationality (ISO 3166-2 Country Code)

place\_of\_birth

string

City or other relevant location of the account holder's birth place

date\_of\_birth

string (date)

Date of birth of the customer in YYYY-MM-DD

gender

string

The gender of the account holder

Valid values[
"MALE",
"FEMALE",
"OTHER"
]

tax\_identification\_number

string

Tax Identification Number of the account holder. This parameter is required when they need to activate Cards capabilities with USD or recurring capabilities.

Please see more details [here](https://docs.xendit.co/docs/activate-payment-channels)

address

object (address)

An address object.

country

string Required

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

city

string Required

City, village or town

province\_state

string Required

Province, state or region

street\_line1

string Required

Line 1 of street address e.g street number and name

Max length255

street\_line2

string Required

Line 2 of street address e.g building name or apartment number

Max length255

district

string Required

District

sub\_district

string Required

Sub-district

postal\_code

string Required

Zip or postal code

address

object (address)

An address object.

country

string Required

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

city

string Required

City, village or town

province\_state

string Required

Province, state or region

street\_line1

string Required

Line 1 of street address e.g street number and name

Max length255

street\_line2

string Required

Line 2 of street address e.g building name or apartment number

Max length255

district

string Required

District

sub\_district

string Required

Sub-district

postal\_code

string Required

Zip or postal code

kyc\_documents

Array of object (kyc\_document)

object

A KYC document file for Account Holder verification

country

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

type

string

The type of the legal or KYC requirements document

Refer to the list of [Required KYC Documents for all countries here](https://docs.xendit.co/docs/create-verification-requests#requirements-by-country-and-entity-type)

expires\_at

string

Expiry date of the document if relevant. Format `YYYY-MM-DD`

file\_id

string

The file ID returned by the Upload API

website\_url

string (website)

A valid website associated with the business

Max length255

Examplemystore.com

phone\_number

string (phone)

A valid phone number associated with the business

Max length30

Example62123456789

email

string (email)

A valid email address associated with the object

Max length255

Exampletest@example.co

capabilities

Array of object

object

type

string

Valid values[
"MONEY\_IN"
]

channel\_code

string

Responses

200

400

403

Show example

application/json

Philippines Corporation

Philippines Corporation

Code snippet

```
{
  "id": "4376b7b0-1c44-46be-8640-828f79cdc8be",
  "business_detail": {
    "type": "CORPORATION",
    "legal_name": "My Store Inc.",
    "trading_name": "John's Store",
    "description": "description here",
    "industry_category": "ELECTRONICS_AND_ACCESSORIES",
    "date_of_registration": "2023-02-02",
    "country_of_operation": "PH"
  },
  "individual_details": [
    {
      "given_names": "John",
      "surname": "Doe",
      "phone_number": "+63021234567",
      "email": "test@xendit.co",
      "nationality": "PH",
      "place_of_birth": "PH",
      "date_of_birth": "2000-02-02",
      "gender": "MALE",
      "type": "PIC",
      "role": "owner"
    }
  ],
  "address": {
    "country": "PH",
    "city": "Caloocan",
    "street_line1": "9th St",
    "street_line2": "Building 101",
    "district": "1st district",
    "sub_district": "2nd subdistrict",
    "province_state": "Metro Manila",
    "postal_code": "1400"
  },
  "kyc_documents": [
    {
      "type": "SEC_CERTIFICATE_REGISTRATION_DOCUMENT",
      "country": "PH",
      "file_id": "63f8719642f5856dcb142bd2"
    },
    {
      "type": "ARTICLES_OF_INCORPORATION_DOCUMENT",
      "country": "PH",
      "file_id": "63f8719642f5856dcb142bd2"
    },
    {
      "type": "NOTARIZED_SECRETARY_CERTIFICATE_DOCUMENT",
      "country": "PH",
      "file_id": "63f8719642f5856dcb142bd2"
    },
    {
      "type": "LATEST_GIS_DOCUMENT",
      "country": "PH",
      "file_id": "63f8719642f5856dcb142bd2"
    },
    {
      "type": "ACR_OR_IMMIGRANT_COR_DOCUMENT",
      "country": "PH",
      "file_id": "63f8719642f5856dcb142bd2"
    },
    {
      "type": "SERVICE_AGREEMENT_DOCUMENT",
      "country": "PH",
      "file_id": "63f8719642f5856dcb142bd2"
    }
  ],
  "website_url": "https://xendit.co",
  "phone_number": "+6381234567",
  "email": "test@xendit.co",
  "kyc": {
    "status": "PASSED",
    "requested_at": "2021-01-01T10:00:00Z",
    "verified_at": "2021-01-02T10:00:00Z",
    "kyc_passed_at": "2021-01-03T10:00:00Z"
  },
  "capabilities": [
    {
      "type": "MONEY_IN",
      "channel_code": "GCASH",
      "requested_at": "2021-01-01T10:00:00Z",
      "verified_at": "2021-01-02T10:00:00Z",
      "activated_at": "2021-01-03T10:00:00Z",
      "status": "VERIFICATION_IN_PROGRESS"
    }
  ]
}
```

JSON

Copy

Collapse all

object

business\_detail

object (business\_detail)

An object containing the business detail of the Account Holder

type

string

The entity type of the business

Valid values[
"CORPORATION",
"PARTNERSHIP",
"SOLE\_PROPRIETORSHIP",
"INDIVIDUAL",
"FOREIGN",
"FOREIGN\_SEC",
"FOREIGN\_NONSEC"
]

legal\_name

string

Legal name of the business. This must match the documentation submitted.

trading\_name

string

Trading or brand name of the business. This will be the name that appears to endpayer on payment page.

description

string

Description of the business. Please specify what business model or goods and services that the business provide. Max 1000 characters.

industry\_category

string

One of our accepted Industry Category Codes depending on your entity type and country of operation.

Refer to the list of [accepted industry category codes here](https://docs.xendit.co/docs/create-verification-requests#list-of-accepted-industry-categories)

date\_of\_registration

string (date)

Business registration date in YYYY-MM-DD

country\_of\_operation

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

individual\_details

Array of object (individual\_detail)

object

An object containing the individual details of the Account Holder. This could be the details of the business owner, director etc.

type

string

At least one individual with the type `PIC` (Person in Charge) is required. You may submit multiple PICs for your business in this object.
A minimum 1 Incorporator and 1 PIC is required when they need to activate Cards capabilities.

Valid values[
"PIC",
"Incorporator"
]

role

string

This role specifies the role of the PIC or Incorporator. E.g. Owner, Director, Administrator.

given\_names

string

First and middle name (if any) of the account holder

Max length255

surname

string

Surname or family name of the account holder

Max length255

phone\_number

string

The contact number of the Account Holder in `E.164` format. This may also be a landline.

Max length30

email

string

The email address of the account holder

Max length255

nationality

string

Country code for customer's nationality (ISO 3166-2 Country Code)

place\_of\_birth

string

City or other relevant location of the account holder's birth place

date\_of\_birth

string (date)

Date of birth of the customer in YYYY-MM-DD

gender

string

The gender of the account holder

Valid values[
"MALE",
"FEMALE",
"OTHER"
]

tax\_identification\_number

string

Tax Identification Number of the account holder. This parameter is required when they need to activate Cards capabilities with USD or recurring capabilities.

Please see more details [here](https://docs.xendit.co/docs/activate-payment-channels)

address

object (address)

An address object.

country

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

city

string

City, village or town

province\_state

string

Province, state or region

street\_line1

string

Line 1 of street address e.g street number and name

Max length255

street\_line2

string

Line 2 of street address e.g building name or apartment number

Max length255

district

string

District

sub\_district

string

Sub-district

postal\_code

string

Zip or postal code

address

object (address)

An address object.

country

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

city

string

City, village or town

province\_state

string

Province, state or region

street\_line1

string

Line 1 of street address e.g street number and name

Max length255

street\_line2

string

Line 2 of street address e.g building name or apartment number

Max length255

district

string

District

sub\_district

string

Sub-district

postal\_code

string

Zip or postal code

kyc\_documents

Array of object (kyc\_document)

object

A KYC document file for Account Holder verification

country

string

The country (based on ISO 3166-1 Alpha-2) of incorporation for a business, or the country of residence for an individual.

Valid values[
"ID",
"PH",
"VN",
"MY",
"TH"
]

type

string

The type of the legal or KYC requirements document

Refer to the list of [Required KYC Documents for all countries here](https://docs.xendit.co/docs/create-verification-requests#requirements-by-country-and-entity-type)

expires\_at

string

Expiry date of the document if relevant. Format `YYYY-MM-DD`

file\_id

string

The file ID returned by the Upload API

website\_url

string (website)

A valid website associated with the business

Max length255

Examplemystore.com

phone\_number

string (phone)

A valid phone number associated with the business

Max length30

Example62123456789

email

string (email)

A valid email address associated with the object

Max length255

Exampletest@example.co

capabilities

Array of object (account\_holder\_capability\_response)

object

An object containing the details of the Account Holder capabilities activation process

type

string

channel\_code

string

status

string

Valid values[
"LIVE",
"VERIFICATION\_IN\_PROGRESS",
"RESUBMISSION\_REQUIRED",
"DECLINED"
]

failure\_reason

string

activated\_at

string (date-time)

Timestamp of when the object was updated

verified\_at

string (date-time)

Timestamp of when the object was updated

requested\_at

string (date-time)

Timestamp of when the object was updated

kyc

object (account\_holder\_kyc\_response)

status

string

Valid values[
"PASSED",
"FAILED",
"RESUBMISSION\_REQUIRED"
]

requested\_at

string (date-time)

Timestamp of when the object was updated

kyc\_passed\_at

string (date-time)

Timestamp of when the object was updated

verified\_at

string (date-time)

Timestamp of when the object was updated

Show example

application/json

INSUFFICIENT\_ACCOUNT\_HOLDER\_DATA

INSUFFICIENT\_ACCOUNT\_HOLDER\_DATA

Code snippet

```
{
  "error_code": "INSUFFICIENT_ACCOUNT_HOLDER_DATA",
  "message": "The information in the Account Holder object is not sufficient to request activation for this payment channel. Please update the fields with the correct information.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

object

Inputs are failing validation. The errors field contains details about which fields are violating validation.

error\_code

string

Valid values[
"API\_VALIDATION\_ERROR",
"INVALID\_CONFIGURATION",
"INVALID\_JSON\_FORMAT",
"TYPE\_AND\_CONFIGURATION\_CONFLICT",
"INVALID\_SOURCE\_OR\_DESTINATION\_ERROR",
"INSUFFICIENT\_BALANCE",
"INVALID\_FEE\_AMOUNT",
"DUPLICATE\_ERROR",
"INVALID\_AMOUNT",
"INSUFFICIENT\_ACCOUNT\_HOLDER\_DATA",
"MISMATCH\_PAYLOAD\_FOR\_REFERENCE",
"INVALID\_URL\_FORMAT"
]

message

string

errors

Array

OneOf

string

string

object

object

Show example

application/json

KYC\_VERIFICATION\_IN\_PROGRESS
CHANNEL\_HAS\_BEEN\_ACTIVATED

KYC\_VERIFICATION\_IN\_PROGRESS

Code snippet

```
{
  "error_code": "KYC_VERIFICATION_IN_PROGRESS",
  "message": "Account Holder cannot be updated while KYC verification is in progress, please try again when the verification process has been completed.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

CHANNEL\_HAS\_BEEN\_ACTIVATED

Code snippet

```
{
  "error_code": "CHANNEL_HAS_BEEN_ACTIVATED",
  "message": "The payment channel requested has already been activated for this account holder.",
  "errors": [
    "Detailed description here"
  ]
}
```

JSON

Copy

object

Forbidden request

error\_code

string

Valid values[
"REQUEST\_FORBIDDEN\_ERROR",
"FEATURE\_NOT\_ACTIVATED",
"DUPLICATE\_REFERENCE",
"XEN\_PLATFORM\_SUB\_ACCOUNT\_NOT\_LIVE",
"API\_KEY\_ENVIRONMENT\_NOT\_MATCH",
"CHANNEL\_ACTIVATION\_IN\_PROGRESS",
"CHANNEL\_HAS\_BEEN\_ACTIVATED",
"KYC\_VERIFICATION\_IN\_PROGRESS"
]

message

string

errors

Array

OneOf

string

string

object

object

Was this article helpful?

Yes  No

Previous article

Get account holder

Next article

Get transfer by reference

- Try It
- Code samples

Authentication

Username\*

Password (optional)

Request

URL

id \*

Body

application/json

application/json

Update Website

Update Website

Update KYC Document

Activate Payment Channel Capabilities

 Reset to default

 

3

1

```
{
```

2

```
  "website_url": "valid-marketplace.brand.com"
```

3

```
}
```

 Try it & see response

Response

Available responses

application/json

application/json

200400403

 

```
   "activated_at": "2026-04-23T07:10:49.027Z",
```