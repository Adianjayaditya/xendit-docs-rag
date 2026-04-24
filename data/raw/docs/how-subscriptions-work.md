---
url: https://docs.xendit.co/docs/how-subscriptions-work
title: How subscriptions work
description: ''
section: docs
scraped_at: '2026-04-23T06:30:20.437858Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsPayment productsSubscriptions
- Documentation
- Accept payments
- Payment products
- Subscriptions
---
# How subscriptions work

Subscriptions allows you to manage recurring payments with flexibility and ease, be it weekly, monthly, or yearly. Beyond automated scheduling, Subscriptions is designed to enhance the end-user experience and improve payment success rates with advanced features, ensuring an efficient subscription management process with low-cost integration.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Subscriptions-overview.drawio.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A30%3A16Z&se=2026-04-23T06%3A42%3A16Z&sr=c&sp=r&sig=5I9F7A0RkOAlNxfSYrS4e4KZYIOTFoYpwlQGcdh%2FlJA%3D)

## Solutions

You can set up recurring payment plans for your end users with ease. Simply define the amount, schedule, and [recovery options for failed payments](/v1/docs/recover-failed-payments), and Xendit will handle the scheduling and automatic deductions. All you need to do is monitor webhook events to track payment confirmations for each billing cycle.

## Create subscriptions on the dashboard

> This feature currently only available for our legacy subscription product
>
> Please visit our [migration guide](/v1/docs/migrate-from-legacy-subscriptions-to-new-subscriptions) pages here for more details

**Before you begin**

To create a subscription plan, you must have at least one active payment channel that supports Merchant-Initiated Transactions.

- **Check compatibility:** Go to the [Available Payment Channels table](/v1/docs/available-payment-channels) and apply the Merchant-Initiated Transaction filter to see which channels support this.
- **Activation:** Please note that some payment channels may not be available for self-activation via the Dashboard. In these cases, please contact our CS for assistance.
- For more information on how to activate payment channels, please [click here](/v1/docs/activate-payment-channels).

**How to create a subscription**

1. Go to the **Subscriptions** page
2. Click **Create Plan**
3. Enter the **plan details**, such as your customer's info and the amount to charge
4. Select **subscription cycle** (weekly, monthly, etc.).
5. Configure **retry settings** for failed payments to maximize success rates
6. (Optional) Choose how to notify your customer about payments (i.e. email, SMS)
7. Click **Create Plan**
8. Share the payment link with your customer

Once your customer links their auto-debit payment method, their subscription will start automatically.

You can also download reports from the Xendit Dashboard to keep track of your subscriptions.

## Create subscriptions via API integration

There are 2 entry points of creating subscriptions via our API:

1. **Xendit Checkout UI**

   Use this entry point if you want to use Xendit’s hosted UI (via Payment Link or components) to collect and tokenize your user's payment method during the subscription setup.
2. **Existing Payment Token\**Use this entry point if you already have an existing payment token ID for your customer and want to create a subscription plan immediately.

Xendit Checkout UI

Existing Payment Token

- **Create Payment Session**: Create a Payment Session with the type `SUBSCRIPTION`. In this request, you will define all critical subscription parameters, including amount and currency, billing cycle, anchor date, payment schedule, customer information and retry configuration
- **Redirect User**: Redirect your user to the URL of payment link or via Component  to proceed with the payment/linking process.
- **Webhooks**: Once the session is successfully completed, you will receive:

  - Payment Session completion, indicating the complete state of the current session
  - Payment Token Webhook for the new payment method.
  - Subscription Plan Webhook notification, indicating that the plan is active.
- **Management**: Xendit will automatically start managing the schedule and deduct the user's balance based on the defined plan. Listen to our webhook notification on the cycle of the subscription.

- **Create Subscription Plan**: You will create the subscription plan by providing the `payment_token_id` you already have.
- **Webhooks**: Once the subscription request is completed, you will receive a Subscription Plan Webhook notification.
- **Management**: Xendit will automatically start managing the schedule and deduct the user's balance based on the defined plan. Listen to our webhook notification on the cycle of the subscription.

[You can find the detailed integration guide here.](/v1/docs/subscriptions-overview)
