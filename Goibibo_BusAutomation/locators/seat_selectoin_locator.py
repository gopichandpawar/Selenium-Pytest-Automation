class SeatSelectLocator:
    SEAT_SELECT = "(//div[starts-with(@class,'BusBerthstyles__BusOutline-sc')]//div)[12]"
    BOARDING_POINT = "(//div//label[starts-with(@class,'RadioButtonstyles__RadioLabel')])[1]"
    CONTINUE2 = "(//div//button[text()='CONTINUE'])[1]"