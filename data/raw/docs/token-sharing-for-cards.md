---
url: https://docs.xendit.co/docs/token-sharing-for-cards
title: Token sharing for cards
description: ''
section: docs
scraped_at: '2026-04-23T06:17:50.272421Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformAccept & Route Payments
- Documentation
- xenPlatform
- Accept & Route Payments
---
# Token sharing for cards

If you are integrating with our legacy [Cards Charge API](https://archive.developers.xendit.co/api-reference/#create-charge), you can also request to have Token Sharing enabled so that you can tokenize and create charges with different accounts, whether it’s the master account or one of your sub-accounts. Without this feature activated, only the account that tokenizes the card can create the charge.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xp-cards-token-sharing.drawio.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A17%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=Rmz%2FNod10FzSaiprQW32CPAHP9w94mNK08B1wjqBYjg%3D)

xenPlatform Token Sharing Illustration

Please note that token sharing only works with multi-use tokens.

> Limited Availability
>
> Please contact your Account Manager to request for this feature. If you are sharing tokens across different entities, we require the following consent to be collected during the end-user’s payment:
>
> 1. Privacy Policy: You must mention that your Master Account will be sharing personal data collected with Xendit
> 2. Terms of Service: Add a reference to Xendit's Terms and Conditions that the merchants must agree to for using our services

## API Guide

1. [Follow this guide](https://archive.developers.xendit.co/api-reference/#create-token) to tokenize when a customer submits their credit card information

   1. If you are making a request on behalf of a sub-account, set the `for-user-id` to the sub-account business ID. Leave this header out if you are tokenizing from the master account.
   2. Make sure to set `is_multiple_use` to true
2. Store the returned `credit_card_token_id` in your system
3. When a customer makes a purchase, you can now [authenticate](https://archive.developers.xendit.co/api-reference/#create-authentication) and [charge](https://archive.developers.xendit.co/api-reference/#create-charge) the customer’s card

   1. If you are making a request on behalf of a sub-account, set the `for-user-id` to the sub-account business ID. Leave this header out if you are charging from the master account.
4. With the token sharing feature activated, the charge should be successful even if the token was created on a different account
