---
url: https://docs.xendit.co/docs/payout-coverage-indonesia
title: Indonesia
section: docs
product: xendit
---
## Overview

| Payout Rail | Local - BI Fast | Local - RTGS |
| --- | --- | --- |
| Supported Currencies | IDR | IDR |
| Estimated Time of Arrival | 15 minutes | 2 hours |
| Cut-off Time | N/A | 14:00 GMT+7 |
| Transaction Limit | 250,000,000 | Unlimited |
| Description Support | Yes | Yes |
| Supported Use Case | - Payout - Cross Border Payout - Payout Link | - Payout - Cross Border Payout - Payout Link |

## Channel Codes

Learn the different payout destinations that we support along with its destination-specific information in the table below:

## Required Values for Cross-Border Payouts

As a prerequisite to creating a Cross-Border Payout, you are required to send us the ultimate sender and recipient’s information. Learn the required information for the region to start sending payouts:

### Sender

| Field Parameter | Type | Description |
| --- | --- | --- |
| `individual_detail.given_names` | `INDIVIDUAL` | First name of sender |
| `individual_detail.surname` | `INDIVIDUAL` | Last name of sender |
| `business_detail.business_name` | `BUSINESS` | Full registered name of sender |
| `addresses.country` | Any | Country Address of Sender |
| `addresses.street_line1` | Any | Full Address of Sender |

### Recipient

| Field Parameter | Type | Description |
| --- | --- | --- |
| `individual_detail.given_names` | `INDIVIDUAL` | First name of recipient |
| `individual_detail.surname` | `INDIVIDUAL` | Last name of recipient |
| `business_detail.business_name` | `BUSINESS` | Full registered name of recipient |
| `identity_accounts.type` | Any | Account type of the recipient’s account |
| `identity_accounts.company` | Any | Channel code of the recipient’s account |
| `identity_accounts.country` | Any | Issuing country of the recipient’s account |
| `identity_accounts.properties.account_number` | Any | Account number of the recipient’s account detail |
| `identity_accounts.properties.account_holder_name` | Any | Account holder name of the recipient’s account detail |
| `addresses.country` | Any | Country address of the recipient |
| `addresses.city` | Any | City address of the recipient |

## Account length limit

### Bank accounts

The number of digits in a bank account number for each of the banks in Indonesia varies according to the bank. The following is the guideline of bank account length for the top banks in Indonesia.

| **Bank Code** | **Account Number Length** |
| --- | --- |
| BCA | 10 Digits |
| BRI\* | 13-17 Digits |
| BNI | 7-11 Digits |
| MANDIRI\* | 12-17 Digits |
| PERMATA\* | 7-16 Digits |

*\*Note: The number of digits may include the length for Virtual Accounts.*

Notes for BRI : Please make sure to add an extra 0 prefix in the case of a bank accounts with 14 digits. This is not applicable to VA accounts. (eg. 012345678901234)

### E-Wallet Accounts

E-wallet accounts in Indonesia are based on Indonesian mobile numbers. While mobile numbers are usually written to include the country code, when mobile numbers are used as e-wallet account numbers, it is more common to use the format that contains 11 digits and where the prefix starts with zero (0). Example: `0XXXYYYZZZZ`

## Payout Identifier

When creating a payout, you can also include a unique identifier (e.g. Order ID, your business name, etc.) in the `description` field. If your recipient's bank supports it, they'll see this in their transaction history. Otherwise, they’ll see Xendit’s sender name. Note that character limits vary by bank, so keep your identifier short.

| **Destination Channel** | **Amount** | **Max. Characters** |
| --- | --- | --- |
| BCA | Less than IDR 9,999 or more than IDR 50,000,001 | 30 characters |
| BCA | IDR 10,000 - IDR 50,000,000 | 15 characters |
| BRI | Any amount | 29 characters |
| BNI | Any amount | 14 characters |
| MANDIRI | Any amount | 14 characters |
| PERMATA | Any amount | 20 characters |
| CIMB | IDR 10,000 - IDR 50,000,000 | 18 characters |
| MAYBANK | IDR 10,000 - IDR 50,000,000 | 17 characters |
| Other banks | IDR 10,000 - IDR 50,000,000 | Description may not be supported |

## Recipient Interface

### Bank Channels

See below for examples of what is shown in your recipient’s bank statement. If supported, the bank statement will display Xendit as sender and the `description` you input.

| **Channel** | **Sample of line on bank statement** |
| --- | --- |
| BCA | TRSF E-BANKING CR 0410/FTSCY/WS95051 1000.00 2NU6g~[Description] SINAR DIGITAL TERD, or SWITCHING CR TRANSFER DR 523 [Description] KPO BSS |
| BNI | TRANSFER DARI XENDIT One Gate Payment #201910090128466362836245 [Description] 201910090128466362836245 SINAR DIGITAL TERDEPAN |
| BRI | ~3SeQr SNR [Description] |
| MANDIRI | 1260007569477 10/10/2019 10/10/2019 7820 MCM InhouseTrf CS-CS DARI SINAR DIGITAL TERDEPAN [Description] #2PmKJ 0 123 |

### E-Wallet Channels

See below for examples of what shows up on your recipient's e-wallet apps. If supported, the app will display Xendit as the sender and the `description` you input.