class ProductLocators:

    PRODUCT = "(//a[@href='/shopping/product?id=1'])[1]"
    QUANTITY = "//select[@id='quantitySelect']"
    BUY = "//button[contains(@id,'buyNowBtn')]"
    PLACE_ORDER = "//a[contains(text(),'Place Order')]"