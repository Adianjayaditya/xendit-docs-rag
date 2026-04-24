---
url: https://docs.xendit.co/docs/xenplatform-global-accounts-setup
title: Create sub-accounts for Global Accounts (Beta)
description: ''
section: docs
scraped_at: '2026-04-23T06:19:26.148726Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformSet up sub-accounts
- Documentation
- xenPlatform
- Set up sub-accounts
---
# Create sub-accounts for Global Accounts (Beta)

If you have set up a [Global Account](/docs/global-account) and have xenPlatform activated, you can start creating sub-accounts to accept payments on their behalf and route funds between all your accounts.

## Creating and verifying sub-accounts

Find the “Create Sub-account” button in the xenPlatform Sub-Accounts page. After providing a business name for the sub-account, you can either:

- Verify the sub-account yourself, if you are the Authorized Representative
- Invite an Authorized Representative who legally represents the business to later submit the verification information

**Note:** Only the Authorized Representative can submit the business verification form once it’s filled in. They are also required to complete a Liveness Verification test. The person creating the sub-account can also access the verification form at any time.

### Additional Configurations

You will also need to specify how webhooks are sent for events occurring in your sub-accounts. You can set this to either use the Master account’s configured webhook URLs (synchronized), or use the sub-account’s configured webhook URLs.

### Using the API

Our [Create Account API](https://docs.xendit.co/apidocs/create-account) can also be used to automate the sub-account creation process. You can refer to [this guide](/docs/create-sub-accounts#creating-subaccounts-via-api) for more details.

To pass on KYC information and verify sub-accounts using the API, refer to [this guide](/docs/xenplatform-verification-api).

## Next steps

After your sub-accounts have gone Live, you can follow our [guide](/docs/accepting-payments-for-sub-accounts) to start accepting payments or [create Split Rules](/docs/split-payments) to transfer a portion of the payment amounts to different accounts.

##
