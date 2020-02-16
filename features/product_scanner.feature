Feature: Product scanner
    A user can scan a QR-code or a barcode of a product in order to get additional information in digital format 
        or put this information in required fields of an app

Scenario: getting information about product calories
    Given a user has a package of oat flackes with description in foreign language
    When the user scannes a QR-code or a barcode of the product
    Then the system opens up a window with information about amount of calories and the proportion of proteins, fats and carbohydrates 
        of the product


Scenario: creation of a planned menu
    Given a user bought 15 meal products for the week
    When the user scannes a QR-code or a barcode of the product
    Then the system creates a planned menu that can be used in the future when the user will add a new 
        record in a diary


Scenario: extensive insert in a planned menu
    Given a user has a receipt from the grocerie store
    When the user scannes a QR-code of the receipt
    Then the system shows a window with the list of products that can be added in the planned menu