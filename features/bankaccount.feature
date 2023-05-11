Feature: Bank account

    Scenario: Deposit into account
        Given an bank account exists
        When depositing money
        Then balance should be increased