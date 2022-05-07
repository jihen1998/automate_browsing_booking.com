from booking.booking import Booking
""" inst = Booking("D:\herodot\chromedriver")
inst.land_first_age() """
with Booking("D:\herodot\chromedriver") as bot:
    bot.land_first_age()
    bot.change_currency(input("enter currency : "))
    bot.enter_city(input("enter the desired city :  "))
    bot.choose_check_it_out_date(input("checkin date : "),input("checkout date : "))
    bot.Add_adult(int(input("how many adults? ")))
    bot.view_results()
    bot.do_filration()
    bot.refresh()
    bot.report_result()
    print("exit...")
""" once pyhhon gets out of identation of with then it execute automatically the __exit__ """