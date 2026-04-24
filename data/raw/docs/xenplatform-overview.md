---
url: https://docs.xendit.co/docs/xenplatform-overview
title: Overview
description: ''
section: docs
scraped_at: '2026-04-23T06:07:37.397665Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatform
- Documentation
- xenPlatform
---
# Overview

xenPlatform is a payment solution for platform businesses that need to manage funds for multiple merchants. Think of it like a central hub for handling all your platform's payment needs.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xp-tree-gif.gif?sv=2022-11-02&spr=https&st=2026-04-23T06%3A07%3A34Z&se=2026-04-23T06%3A19%3A34Z&sr=c&sp=r&sig=gq8scCrC7xHJa52YHMHORC26iweP5qDfpIZqIpCEP2Q%3D)

xenPlatform enables your business to:

- Create and manage individual sub-accounts for each merchant.
- Accept payments on behalf of your merchants.
- Split payments between multiple accounts.
- Track all transactions in one place.
- Pay out to your merchants’ bank accounts.

This simplifies complex payment flows for businesses like:

- **Marketplaces:**  E-commerce platforms with multiple sellers.
- **SaaS Platforms:**  Subscription services with various vendors.
- **Brick-and-mortar:** Businesses operating multiple physical stores with unified payment systems.
- **Other platforms:**  Any business model with multiple partners receiving funds.

## xenPlatform Terminology

- **Master Account:** Your Xendit account with xenPlatform activated, and can create sub-accounts. We also refer to multi-account businesses as Platforms.
- **Sub-Account:** The Xendit account where transactions are processed for your merchants. Each account has a separate balance and transaction history. The entity represented by the sub-accounts can be your merchants, partners, sellers, vendors, branches, drivers, etc.

### Account IDs for API Requests

An Account ID is the account identifier used for various requests (card charges, payouts, reports, etc.). It is how you can identify which sub-account you wish to perform the requests for. In our API references, there are synonyms to an Account ID which are: `user-id` , `owner_id` , `business_id` .

## Use Cases

Using xenPlatform to manage payments for sub-accounts involves 4 simple steps:

1. Creating a sub-account
2. Managing their payments
3. Monitoring their transactions
4. Paying out

In each step, there are different options that you can choose based on the payments experience that you want to provide to your merchants. We have created several suggested recipes for common business models:

| Business Models | Examples | Account Setup | Payment Routing |
| --- | --- | --- | --- |
| Payment Service Providers | Helixpay, Tazapay | Flexibly determine the right setup based on onboarding policies and license requirements | 1. Accept payments on behalf of your Partners by building your own payment page with our range of payment options via API 2. Create Split Fees to automate charging commissions per transaction 3. [Pay out](/docs/payouts-for-sub-accounts) or allow merchants to withdraw their own funds |
| SaaS Platforms | TADA, Qoala | Onboard merchants at-scale using the API and control funds on their behalf | 1. Create sub-accounts via API using the `OWNED` type 2. Accept payments on behalf of your merchants by using our hosted checkout solution for easy integration 3. Create Split Fees to automate charging commissions per transaction 4. [Disburse](/v1/docs/payouts-for-sub-accounts) funds to your merchants’ bank accounts |
| Point-of-Sale Platforms | ESB, Raptor POS | Invite other merchants as sub-accounts to allow them to manage their own payments | 1. Accept payments on behalf of your Partners by building your own payment page with our range of payment options via API 2. Create Split Fees to automate charging commissions per transaction 3. Merchants can withdraw their own funds to their bank accounts |
| Brand Conglomerates | XL, Ciputra Group | Invite branch or subsidiaries as sub-accounts to allow them to manage their own payments | 1. Each branch or subsidiary operates their own dashboard to accept payments from customers, monitor transactions and withdraw. 2. Use [Transfers](/docs/transfer-balances) to move balances from subsidiaries to the Platform account as needed. |
