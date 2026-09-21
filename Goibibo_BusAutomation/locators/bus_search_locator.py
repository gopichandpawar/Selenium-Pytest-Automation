class BusSearchLocator:
    FROM_INPUT = "//input[@id='autosuggestBusSRPSrcHome']"
    FROM_SUGGEST_INPUT = "//span[text()='Pune, Maharashtra']"
    TO_INPUT = "//input[@id='autosuggestBusSRPDestHome']"
    TO_SUGGEST_INPUT = "//span[text()='Yavatmal, Maharashtra']"
    SEARCH_BUS = "//button[@data-testid='searchBusBtn']"
