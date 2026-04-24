---
url: https://docs.xendit.co/docs/batch-payouts-beta
title: Global Batch Payouts (Beta)
description: ''
section: docs
scraped_at: '2026-04-23T06:21:30.862934Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationSend moneyPayout productsPayouts (Disbursements)
- Documentation
- Send money
- Payout products
- Payouts (Disbursements)
---
# Global Batch Payouts (Beta)

> **Rolling out to Global Account users**
>
> We’ll send you an email once we’ve rolled the feature out to you.

Our Batch Payouts feature lets you send up to 1,000 payouts across the globe simultaneously with a single Excel file upload, saving you significant time and resources. This is perfect for bulk payments like salaries, supplier payments, or earnings distribution.

This solution requires no code integration for a seamless and efficient payout experience.

## How to create a Batch Payout

> **Important Note**
>
> To create a payout via dashboard, you must have an `Edit` user role.

Navigate to **Send Payments** > [**Payouts**](https://dashboard.xendit.co/payouts), and click **Create Payout**. Follow these easy steps below.

#### 1. Download the template

Download the newest template version. You can fill out up to 1,000 payout transactions in the batch payout template file.

#### Template File

The downloaded batch template Excel file consists of 2 worksheets:

1. **Guideline** - Instructions for your reference. Read this to start.
2. **Template** - Template for you to fill in the transfer details.

To help you, we’ve color-coded the template columns. The blue columns are required to process the payout, the yellow columns are conditional, while the grey columns are optional.

#### 2. Upload filled template

Once you’ve listed all of your payout transactions in the template file, upload the batch file by selecting it or dragging it inside the upload area.

#### 3. Input batch reference

Batch Reference is used as a reference to identify your different batch payouts and help you with reconciliation. While it is possible to use the same reference, we recommend you to use different batch reference for all your batch payouts.

#### 4. Select Source Currency

Select the source currency balance that will be debited when the batch is processed. Ensure you have sufficient balance.

#### 5. Select Approval Workflow

> **Important Note**
>
> To create an Approval Workflow, you must have an `Admin` user role.

To ensure the security of your payouts, you will need to select an Approval Workflow that you have set up. If you have no existing Approval Workflow, you can create one by clicking **Create Approval Workflow**.

The selected Approval Workflow would dictate which of your team members would be allowed to approve the batch.

#### 6. Enable account name check (Optional)

Xendit account name check feature allows you to verify the recipient's account number and the account's name with the bank's database. This allows you to:

- Check if the account number that you've filled is valid
- Check on whether the account name you've filled matches the name of the account provided by the bank

***\*Currently available for ID and VN accounts***

#### 7. Click Create button

Once you’ve done everything, click **Create** to create your batch payout!

## Validate a Batch Payout

Once a batch payout has been successfully created, we automatically validate transaction details to check for errors to pre-empt wrong or failed payouts. If an error is found in the transaction, the batch will require validation and will have the status `Need Review`. You can fix all the issues directly on the Dashboard before proceeding with the transfer.

If no transactions need to be validated, you can directly move to [Review and Approve a Batch Payout](/v1/docs/batch-payouts#review-and-approve-a-batch-payout).

Transactions that require validation will be highlighted for your attention and can be edited by clicking **Review Payout** or directly in the specific payout. Once it has been edited, you may click **Save & Validate**.

Once all of the invalid transactions are resolved, your batch would automatically change status to `Need Approval`.

#### Validation Errors

On this page, you need to validate the transaction/s which need to be validated. There are 2 statuses:

1. **Validated** - This status is for transactions that have been successfully validated
2. **Need Review** - This status is for transactions that need to be edited and validated

## Review and Approve a Batch Payout

> **Important Note**
>
> To approve a payout via dashboard, you must have an `Approver` user role.

Once you’ve reviewed all the transaction details, you can submit the batch for approval. Transactions that have been successfully validated will have the `Need Approval` status.

An approver can only approve the batch using their 6-digit PIN, for enhanced security. To note, if you are converting currencies, the rate shown before approving is indicative. Rate used will be using live market rate when the transaction is processed.

Once you approve the batch, Xendit will process the payouts immediately. Please note that once submitted, payouts are final and cannot be amended or reversed. We are also unable to correct bank names or account numbers after a batch has been submitted.

You can also opt to reject the batch if you don’t want it to be processed. You will be prompted to optionally fill in a reason for the rejection. This reason will be shown in the batch payout’s detail page.

## Track your Batch Payout

Once approved, we will process your batch payout where its status will be `Disbursing`. To monitor each payout’s status within an approved batch payout, follow below easy steps:

1. Go to **Send Payment** > [**Payouts**](https://dashboard.xendit.co/payouts)
2. Select a batch payout
3. View the status of each payout

## Batch Payout Statuses

Batch Payout has its own status that will help you to easily identify which batch are already completed, failed, or is still in process by Xendit. These are the possible statuses a batch payout can have:

| **Status** | **Description** |
| --- | --- |
| `Need Review` | Some payouts within the batch requires your review. Commonly missing field. |
| `Need Approval` | The batch payout is ready to be processed and pending approval |
| `Disbursing` | Batch payout is approved and payouts are being processed |
| `Completed` | All payouts within the batch has been processed. To note, the batch may contain both Successful and/or Failed transactions. |
| `Rejected` | The batch payout has been rejected by the Approver |
| `Failed` | The batch payout failed to be created. Commonly due to bad template. |
