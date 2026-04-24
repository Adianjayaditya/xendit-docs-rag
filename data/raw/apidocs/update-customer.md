---
url: https://docs.xendit.co/apidocs/update-customer
title: "Update Customer"
section: apidocs
product: xendit
---

[Skip to main content](javascript:void(0);)

- [Documentation](https://xendit-docs.document360.io/docs/overview)

  Use ←/→ to navigate

Login

- - [API Documentation](/apidocs)
  - [Others](/apidocs/others-introduction)
  - [Customers](/apidocs/get-customers-list)

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

Webhook Settings

Others

Download API reference

[Introduction](/apidocs/others-introduction)

Customers

get

 [Get customers list](/apidocs/get-customers-list)

post

 [Create customer request](/apidocs/create-customer-request)

get

 [Get customer by id](/apidocs/get-customer-id)

pat

 [Update Customer](/apidocs/update-customer)

Bill Payments

Files

For archived content, access the previous documentation [here](https://archive.docs.xendit.co) or the previous API reference [here](https://archive.developers.xendit.co/).

# Update Customer

- Updated on Apr 1, 2026
- Published on Dec 1, 2025

 [Prev](/apidocs/get-customer-id "Get customer by id")  [Next](/apidocs/get-product-list "Get Product List") 

Patch

/customers/{customer\_id}

Make a PATCH request to this endpoint to update the details on a customer. Only fields present in the request will be updated. Any changes to fields on the customer object will replace that item in its entirety. If you wish to append to an array, your PATCH request should contain the desired end state array (i.e., both the current content and the new array element to append to it). Pass a NULL value to remove the existing content.

Note that the reference\_id and type on a customer cannot be updated.

Security

HTTP

Type Basic

Header parameters

api-version

string

API version in date semantic. Attach this parameter when calling a specific API version. List of API versions can be found here.

Valid values[
"2020-10-31",
"2020-05-19"
]

for-user-id

string

The sub-account user-id that you want to make this transaction for.

This header is only used if you have access to xenPlatform. See xenPlatform for more information

Path parameters

customer\_id

stringRequired

Your identifier for the customer

Max length41

Examplecust-b98d6f63-d240-44ec-9bd5-aa42954c4f48

Body parameters

application/json

Collapse all

object

Patch body request

individual\_detail

object (XenditStandardIndividualDetail)

JSON object containing details of the Individual. Required if type is `INDIVIDUAL`

given\_names

string Required

Primary or first name/s of customer. Alphanumeric. No special characters is allowed.

Min length1

Max length50

surname

string | null

Last or family name of customer. Alphanumeric. No special characters is allowed.

Min length1

Max length50

nationality

string | null

Country code for customer nationality. ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

place\_of\_birth

string | null

City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed.

Min length1

Max length60

date\_of\_birth

string | null

Date of birth of the customer. Format: YYYY-MM-DD

Min length10

Max length10

gender

string | null

Gender of customer

Valid values[
"MALE",
"FEMALE",
"OTHER"
]

employment

object | null

employer\_name

string

Name of the employer

Min length1

Max length50

nature\_of\_business

string

Industry or nature of business

Min length1

Max length50

role\_description

string

Occupation or title

Min length1

Max length50

business\_detail

object (XenditStandardBusinessDetail)

JSON object containing details of the business. Required if type is `BUSINESS`

business\_name

string Required

Name of business

Min length1

Max length50

trading\_name

string | null

Trading name

Min length1

Max length50

business\_type

string

Legal entity type of the business

Valid values[
"SOLE\_PROPRIETOR",
"PARTNERSHIP",
"COOPERATIVE",
"TRUST",
"NON\_PROFIT",
"GOVERNMENT",
"CORPORATION"
]

nature\_of\_business

string | null

Free text description of the type of business this entity pursues

Min length1

Max length50

ExampleEcommerce, Travel

business\_domicile

string | null

Registered country of the business. ISO 3166 format

date\_of\_registration

string (date) | null

Business registration date

mobile\_number

string | null

Supports both E.164 international format (+) and local formats with or without a leading zero.

Min length7

Max length15

phone\_number

string | null

Supports both E.164 international format (+) and local formats with or without a leading zero.

Min length7

Max length15

email

string (email) | null

E-mail address of customer

Min length1

Max length50

addresses

object (XenditStandardAddress)

country

string Required

ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

street\_line1

string

Line 1 of street address e.g., building name and apartment number

Min length1

Max length255

street\_line2

string

Line 2 of street address e.g., building name and apartment number

Min length1

Max length255

city

string

City, village or town of residence of customer

Min length1

Max length255

province\_state

string

Province, state or region of residence of customer

Min length1

Max length255

postal\_code

string

ZIP/Postal Code of customer

Min length1

Max length255

category

string

Address type

Valid values[
"HOME",
"WORK",
"PROVINCIAL"
]

is\_primary

boolean

Defaults to false. Indicates that the information provided refers to the customer's primary address

Defaultfalse

kyc\_documents

Array of object (XenditKYCDocumentsObject)

object

country

string Required

ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

type

string

Generic ID type

Valid values[
"BIRTH\_CERTIFICATE",
"BANK\_STATEMENT",
"DRIVING\_LICENSE",
"IDENTITY\_CARD",
"PASSPORT",
"VISA",
"BUSINESS\_REGISTRATION",
"BUSINESS\_LICENSE"
]

sub\_type

string

Specific ID type for IDENTITY\_CARD types

Valid values[
"NATIONAL\_ID",
"CONSULAR\_ID",
"VOTER\_ID",
"POSTAL\_ID",
"RESIDENCE\_PERMIT",
"TAX\_ID",
"STUDENT\_ID",
"MILITARY\_ID",
"MEDICAL\_ID",
"OTHERS"
]

document\_name

string

Free text description of the type of document (e.g., NIB, SIUP, AKTA). `Characters` alphanumeric. No special characters is allowed.

Max length255

document\_number

string

Unique alphanumeric identity document number or code. `Characters` alphanumeric. No special characters is allowed.

Max length255

expires\_at

string | null

Expiry date, if relevant

Example2024-11-11

holder\_name

string

Free text to capture the full name(s) of the individual or business as defined on the document, if relevant. `Characters` alphanumeric. No special characters is allowed.

Max length255

document\_images

Array of string

Array of file ids returned from uploads to the files endpoint, representing images of the front/back of the document, in png/jpg/jpeg/pdf format

string

description

string | null

Merchant-provided description for the customer. `Characters` alphanumeric. No special characters is allowed.

Min length2

Max length500

date\_of\_registration

string (date)

Business registration date

domicile\_of\_registration

string

Country within which the account that the shopper had to create/sign up on the merchant's website resides (e.g. accounts created on Shopee SG have `SG` as the value for this field. ISO 3166-2 Country Code

Min length2

Max length2

metadata

object

Object of additional information related to the customer. Define the JSON properties and values as required to pass information through the APIs.
You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long.
This is only for your use and will not be used by Xendit.

Responses

200

404

Show example

Successful operation

application/json

getIndividualCustomer
getBusinessCustomer

getIndividualCustomer

Code snippet

```
{
  "id": "cust-239c16f4-866d-43e8-9341-7badafbc019f",
  "reference_id": "demo_1475801962607",
  "type": "INDIVIDUAL",
  "individual_detail": {
    "given_names": "John",
    "surname": "Doe",
    "nationality": "ID",
    "place_of_birth": "Jakarta",
    "date_of_birth": "1980-01-01",
    "gender": "MALE",
    "employment": {
      "employer_name": "Xendit",
      "nature_of_business": "Payment Gateway",
      "role_description": "Test dummy"
    }
  },
  "email": "customer@website.com",
  "mobile_number": "+62812123456",
  "phone_number": "+62812123456",
  "hashed_phone_number": "+628#######56",
  "addresses": [
    {
      "street_line1": "Panglima Polim IV",
      "street_line2": "Ruko Grand Panglima Polim, Blok E",
      "city": "Jakarta Selatan",
      "province_state": "DKI Jakarta",
      "postal_code": "993448",
      "country": "ID",
      "category": "HOME",
      "is_primary": true
    }
  ],
  "kyc_documents": [
    {
      "type": "IDENTITY_CARD",
      "sub_type": "NATIONAL_ID",
      "country": "ID",
      "document_name": "KTP",
      "document_number": "12356789012456",
      "expires_at": null,
      "holder_name": "John Doe",
      "document_images": [
        "file-ec700c1c-db17-4496-b1fb-04ebe551b412"
      ]
    }
  ],
  "description": "My first customer",
  "date_of_registration": "2020-03-30",
  "domicile_of_registration": "ID",
  "metadata": {
    "foo": "bar"
  },
  "created": "2020-03-30T06:12:47.212Z",
  "updated": "2020-03-30T06:12:47.212Z"
}
```

JSON

Copy

getBusinessCustomer

Code snippet

```
{
  "id": "cust-239c16f4-866d-43e8-9341-7badafbc019f",
  "reference_id": "demo_1475801962607",
  "type": "BUSINESS",
  "business_detail": {
    "business_name": "ACME Corp",
    "trading_name": null,
    "business_type": "CORPORATION",
    "nature_of_business": null,
    "business_domicile": null,
    "date_of_registration": null
  },
  "email": "customer@website.com",
  "mobile_number": null,
  "phone_number": null,
  "hashed_phone_number": null,
  "addresses": [],
  "kyc_documents": [],
  "description": null,
  "date_of_registration": "2020-03-30",
  "domicile_of_registration": "ID",
  "metadata": {},
  "created": "2020-03-30T06:12:47.212Z",
  "updated": "2020-03-30T06:12:47.212Z"
}
```

JSON

Copy

Collapse all

object

Customer Object

id

string

Xendit unique Capture ID generated as reference for the end user

Max length41

Examplecust-b98d6f63-d240-44ec-9bd5-aa42954c4f48

reference\_id

string

A Reference ID from merchants to identify their request.

Min length1

Max length255

type

string

Type of customer

Valid values[
"INDIVIDUAL",
"BUSINESS"
]

individual\_detail

object

given\_names

string

Primary or first name/s of customer. Alphanumeric. No special characters is allowed.

Min length1

Max length50

surname

string | null

Last or family name of customer. Alphanumeric. No special characters is allowed.

Min length1

Max length50

nationality

string | null

Country code for customer nationality. ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

place\_of\_birth

string | null

City or other relevant location for the customer birth place. Alphanumeric. No special characters is allowed.

Min length1

Max length60

date\_of\_birth

string | null

Date of birth of the customer. Format: YYYY-MM-DD

Min length10

Max length10

gender

string | null

Gender of customer

Valid values[
"MALE",
"FEMALE",
"OTHER"
]

employment

object | null

employer\_name

string

Name of the employer

Min length1

Max length50

nature\_of\_business

string

Industry or nature of business

Min length1

Max length50

role\_description

string

Occupation or title

Min length1

Max length50

business\_detail

object

business\_name

string

Name of business

Min length1

Max length50

trading\_name

string | null

Trading name

Min length1

Max length50

business\_type

string

Legal entity type of the business

Valid values[
"SOLE\_PROPRIETOR",
"PARTNERSHIP",
"COOPERATIVE",
"TRUST",
"NON\_PROFIT",
"GOVERNMENT",
"CORPORATION"
]

nature\_of\_business

string | null

Free text description of the type of business this entity pursues

Min length1

Max length50

ExampleEcommerce, Travel

business\_domicile

string | null

Registered country of the business. ISO 3166 format

date\_of\_registration

string (date) | null

Business registration date

mobile\_number

string | null

Supports both E.164 international format (+) and local formats with or without a leading zero.

Min length7

Max length15

phone\_number

string | null

Supports both E.164 international format (+) and local formats with or without a leading zero.

Min length7

Max length15

hashed\_phone\_number

string | null

Hashed phone number

Min length1

Max length250

email

string (email) | null

E-mail address of customer

Min length1

Max length50

addresses

Array of object (XenditStandardAddress)

object

country

string

ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

street\_line1

string

Line 1 of street address e.g., building name and apartment number

Min length1

Max length255

street\_line2

string

Line 2 of street address e.g., building name and apartment number

Min length1

Max length255

city

string

City, village or town of residence of customer

Min length1

Max length255

province\_state

string

Province, state or region of residence of customer

Min length1

Max length255

postal\_code

string

ZIP/Postal Code of customer

Min length1

Max length255

category

string

Address type

Valid values[
"HOME",
"WORK",
"PROVINCIAL"
]

is\_primary

boolean

Defaults to false. Indicates that the information provided refers to the customer's primary address

Defaultfalse

identity\_accounts

Array of object (IdentityAccount)

object

type

string

Type of identity account

Valid values[
"CREDIT\_CARD",
"DEBIT\_CARD",
"BANK\_ACCOUNT"
]

company

string

Financial institution or company name

description

string

Description of the account

country

string

ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

properties

object

Additional properties specific to the account type

kyc\_documents

Array of object (XenditKYCDocumentsObject)

object

country

string

ISO 3166-1 alpha-2 Country Code

Min length2

Max length2

type

string

Generic ID type

Valid values[
"BIRTH\_CERTIFICATE",
"BANK\_STATEMENT",
"DRIVING\_LICENSE",
"IDENTITY\_CARD",
"PASSPORT",
"VISA",
"BUSINESS\_REGISTRATION",
"BUSINESS\_LICENSE"
]

sub\_type

string

Specific ID type for IDENTITY\_CARD types

Valid values[
"NATIONAL\_ID",
"CONSULAR\_ID",
"VOTER\_ID",
"POSTAL\_ID",
"RESIDENCE\_PERMIT",
"TAX\_ID",
"STUDENT\_ID",
"MILITARY\_ID",
"MEDICAL\_ID",
"OTHERS"
]

document\_name

string

Free text description of the type of document (e.g., NIB, SIUP, AKTA). `Characters` alphanumeric. No special characters is allowed.

Max length255

document\_number

string

Unique alphanumeric identity document number or code. `Characters` alphanumeric. No special characters is allowed.

Max length255

expires\_at

string | null

Expiry date, if relevant

Example2024-11-11

holder\_name

string

Free text to capture the full name(s) of the individual or business as defined on the document, if relevant. `Characters` alphanumeric. No special characters is allowed.

Max length255

document\_images

Array of string

Array of file ids returned from uploads to the files endpoint, representing images of the front/back of the document, in png/jpg/jpeg/pdf format

string

description

string | null

Merchant-provided description for the customer. `Characters` alphanumeric. No special characters is allowed.

Min length2

Max length500

date\_of\_registration

string (date)

Date of which the account that the shopper had to create/sign up on the merchant's website

domicile\_of\_registration

string

Country within which the account that the shopper had to create/sign up on the merchant's website resides (e.g. accounts created on Shopee SG have `SG` as the value for this field. ISO 3166-2 Country Code

Min length2

Max length2

metadata

object

Object of additional information related to the customer. Define the JSON properties and values as required to pass information through the APIs.
You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long.
This is only for your use and will not be used by Xendit.

created

string (date-time)

Customer creation timestamp

updated

string (date-time)

Customer last update timestamp

The provided `id` does not exist. Please review the `id` and try again

application/json

object

error\_code

string

Valid values[
"RATE\_LIMIT\_EXCEEDED"
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

Get customer by id

Next article

Get Product List

- Try It
- Code samples

Authentication

Request

URL

customer\_id \*

api-version 

2020-10-31 

-  2020-10-31  2020-05-19

for-user-id

Body

application/json

application/json

 

54

1

```
{
```

2

```
 "individual_detail": {
```

3

```
  "given_names": "string",
```

4

```
  "surname": "string",
```

5

```
  "nationality": "string",
```

6

```
  "place_of_birth": "string",
```

7

```
  "date_of_birth": "string",
```

8

```
  "gender": "MALE",
```

9

```
  "employment": {
```

10

```
   "employer_name": "string",
```

11

```
   "nature_of_business": "string",
```

12

```
   "role_description": "string"
```

13

```
  }
```

14

```
 },
```

15

```
 "business_detail": {
```

16

```
  "business_name": "string",
```

17

```
  "trading_name": "string",
```

18

```
  "business_type": "SOLE_PROPRIETOR",
```

19

```
  "nature_of_business": "Ecommerce, Travel",
```

20

```
  "business_domicile": "string",
```

21

```
  "date_of_registration": "2026-04-23"
```

22

```
 },
```

23

```
 "mobile_number": "string",
```

24

```
 "phone_number": "string",
```

 Try it & see response

Response

Available responses

application/json

application/json

200404

 

```
 "id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
```