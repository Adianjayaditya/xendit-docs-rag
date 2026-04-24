---
url: https://docs.xendit.co/docs/fixed-amount-subscriptions
title: Fixed amount Subscriptions
description: ''
section: docs
scraped_at: '2026-04-23T06:20:23.602934Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideSubscriptions
- Documentation
- Accept payments
- Integration guide
- Subscriptions
---
# Fixed amount Subscriptions

Fixed amount subscription is the most common type of subscription, where payments are made at fixed intervals and the amount remains the same for each cycle. Common use cases include media subscriptions, insurance premiums, membership fees, or loan repayments.

## How to integrate

Fixed amount subscriptions basically only need single setup upfront during Subscriptions creation and Xendit will then automatically maintain the scheduler up until the Subscriptions reach the final cycle that you desired.

1. Your app will need to display the Subscriptions for the end user to choose the option. This step it should just sit on your system, no interaction yet to Xendit environment. You can do similar like this

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(93).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A20%3A19Z&se=2026-04-23T06%3A34%3A19Z&sr=c&sp=r&sig=L5X9ygvD40SZqJsEqod28IpcVpNDW%2FhfmVACigWb%2F6M%3D "image(93).png")
2. Once the end user choose their desired plan, you can create the Subscriptions plan to Xendit.

   **Example payload:**

   1. Opt 1: If you already have available `payment_token_id`

      | Request - POST /recurring/plans    ``` {     "reference_id": "plan-{{$timestamp}}",       "customer_id": "cust-9694d170-bcc9-48ac-a6a1-fe04478ea627",     "currency": "IDR",     "amount": 10000,     "payment_tokens": [         {             "payment_token_id": "pt-7f570a37-4e1f-4952-85d5-606b59428349",             "rank": 1         }     ],     "schedule": {         "interval": "MONTH",         "interval_count": 1,         "anchor_date": "2026-04-09T23:23:52+07:00",         "total_recurrence": 100,         "retry_interval": "DAY",         "retry_interval_count": 5,         "total_retry": 7,         "failed_attempt_notifications": [             1,             3,             5         ]     },     "immediate_payment": false,     "failed_cycle_action": "RESUME",     "notification_channels": [         "EMAIL",         "EMAIL"     ],     "locale": "en",     "payment_link_for_failed_attempt": true,       "metadata": {         "customKey": "customValue"       },     "description": "Subscription Example 01" } ```   JSON  Copy | Response - POST /recurring/plans    ``` {     "id": "repl_19299f7e-aeb1-4006-a449-645121965efe",     "reference_id": "plan-1775629572",     "customer_id": "cust-9694d170-bcc9-48ac-a6a1-fe04478ea627",     "failed_cycle_action": "RESUME",     "recurring_cycle_count": 0,     "country": "ID",     "currency": "IDR",     "amount": 10000,     "status": "ACTIVE",     "created": "2026-04-08T06:26:12.448Z",     "updated": "2026-04-08T06:26:12.448Z",     "payment_tokens": [         {             "payment_token_id": "pt-7f570a37-4e1f-4952-85d5-606b59428349",             "rank": 1         }     ],     "schedule": {         "interval": "MONTH",         "interval_count": 1,         "total_recurrence": 100,         "anchor_date": "2026-04-09T23:23:52+07:00",         "retry_interval": "DAY",         "retry_interval_count": 5,         "total_retry": 7,         "failed_attempt_notifications": [             1,             3,             5         ],         "created": "2026-04-08T06:26:12.448Z",         "updated": "2026-04-08T06:26:12.448Z"     },     "immediate_payment": false,     "locale": "en",     "notification_channels": [         "EMAIL",         "EMAIL"     ],     "metadata": {         "customKey": "customValue"     },     "description": "Subscription Example 01",     "items": null,     "payment_link_for_failed_attempt": true,     "failure_code": null } ```   JSON  Copy |
      | --- | --- |
   2. Opt 2: If you need Xendit Hosted Page via Payment Session

      | Request - POST /sessions    ``` {     "reference_id": "TEST_{{$timestamp}}",     "customer": {         "reference_id": "test-{{$timestamp}}",         "type": "INDIVIDUAL",         "individual_detail": {             "given_names": "TEST"         }     },     "session_type": "SUBSCRIPTION",     "subscription": {         "schedule": {             "interval": "MONTH",             "interval_count": 1,             "anchor_date": "2026-04-09T23:23:52+07:00",             "total_recurrence": 100,             "retry_interval": "DAY",             "retry_interval_count": 5,             "total_retry": 7,             "failed_attempt_notifications": [                 1,                 3,                 5             ]         },         "immediate_payment": false,         "failed_cycle_action": "RESUME"     }, "currency": "IDR", "amount": 10000, "mode": "PAYMENT_LINK", "country": "ID", "locale": "en", "description": "Insurance Plan Registration", "success_return_url": "https://xendit.co/success", "cancel_return_url": "https://xendit.co/failure" } ```   JSON  Copy | Response - POST /sessions    ``` {     "payment_session_id": "ps-69d5f625da22a3584993b763",     "created": "2026-04-08T06:31:02.078Z",     "updated": "2026-04-08T06:31:02.078Z",     "status": "ACTIVE",     "reference_id": "TEST_1775629861",     "currency": "IDR",     "amount": 10000,     "country": "ID",     "expires_at": "2026-04-08T07:01:01.083Z",     "session_type": "SUBSCRIPTION",     "mode": "PAYMENT_LINK",     "locale": "en",     "business_id": "5f1e60a0abb3a70ffd45e485",     "customer_id": "cust-da1a36cb-e33d-4f62-a34b-256029b5d9c5",     "description": "Insurance Plan Registration",     "subscription": {         "schedule": {             "interval": "MONTH",             "interval_count": 1,             "anchor_date": "2026-04-09T23:23:52+07:00",             "total_recurrence": 100,             "retry_interval": "DAY",             "retry_interval_count": 5,             "total_retry": 7,             "failed_attempt_notifications": [                 1,                 3,                 5             ]         },         "immediate_payment": false,         "failed_cycle_action": "RESUME"     },     "success_return_url": "https://xendit.co/success",     "cancel_return_url": "https://xendit.co/failure",     "recurring_plan_id": "repl_8eb75eae-30eb-40d9-a420-423e88b703e3",     "payment_link_url": "https://dev.xen.to/a5LftpcH" } ```   JSON  Copy |
      | --- | --- |
3. After creating a subscription, redirect your user to the Xendit-hosted page using the `payment_link_url` or render from the component object from the API response. This step allows the end user to link their payment method to the subscription plan.
4. Once the end user successfully links their payment method, Xendit will send a `recurring.plan.activation` webhook to confirm the activation of the subscription plan.
5. Listen to the cycle webhooks (`recurring.cycle`) to track the status of each subscription cycle. Continue monitoring until all cycles are completed to ensure seamless execution and visibility into the subscription process.

For fixed-amount subscriptions, minimal setup is required on your end. Once the subscription is created, Xendit will automatically process each cycle according to the defined schedule until all cycles are completed.
