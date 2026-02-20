import random
import time
ChaosEvent = True
ChaosEventChance = 15
SeeKarma = False
Win1 = 0
Win2 = 0
Win3 = 0
BanksPacience = 10
BulkBuy = 1
TaxEvasionControl = False
WeirdMessage = True

Assets = {
    "Money": 50,
    "Land Available": 1,
    "Company_Karma": 5,
    "Discoveries": 0,
    "Butt Coin": 0,
    "Tree Dead": 0,
    "Space Available": 0,
    "Total Workers": 0,
    "GrinderBooster": 0,
    "GrinderBooster2": 0
}
Upgrade = {
    "Generator": 0,
    "Big Generator": 0,
    "Studio": 0,
    "Big Studio": 0,
    "PR Headquarter": 0,
    "Lab": 0,
    "Big Lab": 0,
    "Space Headquarters": 0,
    "Rocket Ship": 0,
    "Space Station": 0
}
Investments = {
    "Construction Fund": 0,
    "Insurance": False,
    "FutureTrustFund": False
}
Bank = {
    "Money Owed": 0,
    "Interest Rate": 0
}
Lawyers = {
    "Financial": 0,
    "Property": 0,
    "Protection": 0
}
Workers= {
    "Low pay worker": 0,
    "Medium pay worker": 0,
    "High pay worker": 0

}
Extras = {
    "PrShouting": "Nothing",
    "Tree Dead": 0
}
Law = {
    "TaxEvaded": 0,
    "BlackMarketBought": 0,
    "Illegal Logging": 0,
    "Reputation": "Clean"
}
Shop = {
    "GrinderBooster": 1,
    "GrinderBooster2": 1,


}
EvilTruthRoll = random.randint(1, 3)
GoodTruthRoll = random.randint(1, 3)
EvilLieRoll2 = random.randint(1, 5)
GlazingThySelfRoll = random.randint(1, 3)
BankHit = random.randint(1, 30)
Battle = 0
JailTime = 0
def Lawsuit(power, charge):
    Battle = 0
    print("The goverment is suing you for illegal deeds. SUIT STARTS.")
    time.sleep(5)
    for i in range(3):
        if Lawyers["Protection"] > power:
            print(
                "My sir, the client is clearly innocent due to the complex factors that we have to bring to our attention in this current time frame of the suit.")
            Battle += 1
    if Battle <= 0:
        JailTime = random.randint(500, 2000)
        print("GUILTY!")
        Assets["Money"] -= charge
        Law["TaxEvaded"] = 0
        print("You're going to jail for", JailTime,"seconds.")
    else:
        BankHit = random.randint(1, 30)
        if BankHit == 1:
            JailTime = random.randint(1, 500)
            print("GUILTY! No amount of lawyers can save you from your crimes punk.")
            Assets["Money"] -= charge
            Law["TaxEvaded"] = 0
            print("You're going to jail but your lawyers seem to have decreased penalty to", JailTime, "seconds.")

        else:
            print("The Defendant is innocent")



def LawSystem():
    BankHit = random.randint(1, 30)
    if Law["TaxEvaded"] > 50:
        if BankHit == 1:
            print("YOU HAVE BEEN SUED FOR TAX EVASION")
            Lawsuit(random.randint(1000, 5000), (Assets["Money"] * 0.8))
        else:
            print("")
    elif Law["Illegal Logging"] > 10000:
        if BankHit == 1:
            print("You have been sued for cutting trees... yawn")
            Lawsuit(random.randint(110, 200), 50000000)
        else:
            print("")
    elif Law["BlackMarketBought"] > 10000:
        if BankHit == 1:
            print("You have been sued for buying in sketchy places land, that's a no no.")
            Lawsuit(random.randint(500, 1000), 5000000000)
        else:
            print("")
    elif Workers["Low pay worker"] > Workers["High pay worker"]:
        if Workers["Low pay worker"] > 5000:
            if BankHit == 1:
                print("YOU HAVE BEEN SUED BY ALL YOUR LOW WAGE WORKERS, AND THEY ARE REALLLY MAD!!")
                Lawsuit((Workers["Low pay worker"] / 2), 50000 * Workers["Low pay worker"])
            else:
                print("")


def Tax():
    TaxNumber =(((Upgrade["Generator"] * 5) * ((Bonus1 + Bonus2 + Bonus3) // 3)) + ((Upgrade["Big Generator"] * 10) * ((Bonus1 + Bonus2 + Bonus3) // 3)) + ((Upgrade["Studio"] * 7) * ((Bonus1 + Bonus2 + Bonus3) // 3)) + ((Upgrade["Big Studio"] * 15) * ((Bonus1 + Bonus2 + Bonus3) / 3)) + ((Upgrade["Space Headquarters"] * 30) * ((Bonus1 + Bonus2 + Bonus3) // 3)) + ((Upgrade["Rocket Ship"] * random.randint(0, 1000)) * ((Bonus1 + Bonus2 + Bonus3) // 3)) + ((Upgrade["Space Station"] * 500) * ((Bonus1 + Bonus2 + Bonus3) // 3))) * 0.2
    if TaxEvasionControl == False:
        Assets["Money"] -= TaxNumber
        print("You've been taxed", TaxNumber, ".")
    else:
        print("Your Financial Lawyer sent the money to an offshore account")
        Law["TaxEvaded"] += 1

def Shopping():
    print("(1) Grinder Booster (Makes grinding take 1 second less): 100000000. There's", Shop["GrinderBooster"],
          "in stock")
    print("(2) Grinder Booster 2! (Makes grinding take 1 second less): 10000000000. There's", Shop["GrinderBooster2"],
          "in stock")
    Buy = input("What do you want to buy? (0) to leave")
    if Buy == "1":
        if Shop["GrinderBooster"] > 0:
            Assets["Money"] -= 100000000
            Shop["GrinderBooster"] -= 1
            Assets["GrinderBooster"] += 1
        else:
            print("Sorry that's out of stock")
    elif Buy == "2":
        if Shop["GrinderBooster2"] > 0:
            Assets["Money"] -= 10000000000
            Shop["GrinderBooster2"] -= 1
            Assets["GrinderBooster2"] += 1
        else:
            print("Sorry that's out of stock")
    elif Buy == "0":
        print("Ok, thank you for wasting our time!")
    else:
        print("Invalid Input")





def PrClout():
    EvilTruthRoll = random.randint(1, 3)
    GoodTruthRoll = random.randint(1, 3)
    EvilLieRoll = random.randint(1, 6)
    EvilLieRoll2 = random.randint(1, 5)
    if Extras["PrShouting"] == "Evil Truth":
        if EvilTruthRoll == 1:
            print("WE UNDERPAY WORKERS AND MAKE THEM WORK OVERTIME UNPAID")
            Assets["Company_Karma"] -= 50
        elif EvilTruthRoll == 2:
            print("We have heard customer complaints and worker complaints, we don't give a crap.")
            Assets["Company_Karma"] -= 80
        elif EvilTruthRoll == 3:
            print("Join Us! We pay 100 dollars a day and make you work for 9 hours with no benefits!")
            Assets["Company_Karma"] -= 20
    elif Extras["PrShouting"] == "GoodTruth":
        if GoodTruthRoll == 1:
            print("We focus on the customer first, then our workers, and then our shareholders.")
            Assets["Company_Karma"] += 10
        elif GoodTruthRoll == 2:
            print("We have heard customer complaints and worker complaints, and we are giving them a paid work week off.")
            Assets["Company_Karma"] += 20
        elif GoodTruthRoll == 3:
            print("We want you! We pay 500 - 1000 dollars a day and make you work for 6 hours with medical benefits!")
            Assets["Company_Karma"] += 20
    elif Extras["PrShouting"] == "EvilLie":
        if EvilLieRoll == 1:
            print("A portion of proceeds goes to charity...")
            Assets["Company_Karma"] += 100
            Assets["Money"] -= 1 #this is for charity
        elif EvilLieRoll == 2:
            print("PowerTm Charging your future bright.")
            Assets["Company_Karma"] += 60
        elif EvilLieRoll == 3:
            print("We want you! We pay 5000 - 10000 dollars a day and make you work for 3 hours with medical benefits!")
            Assets["Company_Karma"] += 20
        elif EvilLieRoll == 4:
            print("Our Workers are paid extra!")
            Assets["Company_Karma"] += 180
        elif EvilLieRoll == 5:
            print("Together, we all make the world a better place")
            Assets["Company_Karma"] += 100
        elif EvilLieRoll == 6:
            print("A portion of proceeds goes to growing trees!")
            Extras["Tree Dead"] -= 1
            Assets["Money"] -= 1
            Assets["Company_Karma"] += 500
    elif Extras["PrShouting"] == "EvilLie2":
        if EvilLieRoll2 == 1:
            print("A portion of proceeds goes to charity...")
            Assets["Company_Karma"] += 100
            Assets["Money"] -= 1 #this is for charity
        elif EvilLieRoll2 == 2:
            print("PowerTm Charging your future bright.")
            Assets["Company_Karma"] += 60
        elif EvilLieRoll2 == 3:
            print("We want you! We pay 5000 - 10000 dollars a day and make you work for 3 hours with medical benefits!")
            Assets["Company_Karma"] += 20
        elif EvilLieRoll2 == 4:
            print("Our Workers are paid extra!")
            Assets["Company_Karma"] += 180
        elif EvilLieRoll2 == 5:
            print("Together, we all make the world a better place")
            Assets["Company_Karma"] += 100
    elif Extras["PrShouting"] == "GlazingThySelf":
        if GoodTruthRoll == 1:
            print("We pay hundreds of thousands to our workers")
            Assets["Company_Karma"] += 150
        elif GoodTruthRoll == 2:
            print("We make our products with top of the line quality")
            Assets["Company_Karma"] += 50
        elif GoodTruthRoll == 3:
            print("Our Company Cares most about the consumer.")
            Assets["Company_Karma"] += 200
    else:
        print("")


def PrLies():
    if Upgrade["PR Headquarter"] > 1:
        Lie = input("What do you want to make your pr team say? (1) Truth/(2) Lie").lower()
        if Lie == "1":
            if Workers["Low pay worker"] > Workers["High pay worker"]:
                Extras["PrShouting"] = "EvilTruth"
            else:
                Extras["PrShouting"] = "GoodTruth"
        elif Lie == "2":
            if Workers["Low pay worker"] > Workers["High pay worker"]:
                if Extras["Tree Dead"] > 5000:
                    Extras["PrShouting"] = "EvilLie"
                else:
                    Extras["PrShouting"] = "EvilLie2"
            else:
                Extras["PrShouting"] = "GlazingThySelf"
        else:
            print("Invalid Input")
            return
    else:
        print("You need a Pr Headquarter for this")



def WorkerPay():
    Assets["Money"] -= (100 * Workers["Low pay worker"])
    Assets["Money"] -= (500 * Workers["Medium pay worker"])
    Assets["Money"] -= (1000 * Workers["High pay worker"])
    Assets["Company_Karma"] -= (10 * Workers["Low pay worker"])
    Assets["Company_Karma"] += (5 * Workers["High pay worker"])
    Assets["Money"] -= (1 * (Upgrade["Generator"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (5 * (Upgrade["Big Generator"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (3 * (Upgrade["Studio"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (10 * (Upgrade["Big Studio"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (50 * (Upgrade["Lab"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (120 * (Upgrade["Big Lab"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (25 * (Upgrade["Space Headquarters"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (200 * (Upgrade["Rocket Ship"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))
    Assets["Money"] -= (300 * (Upgrade["Space Station"] * ((Bonus1 + Bonus2 + Bonus3) / 5)))

def worker():
    try:
        WorkerEmployed = int(input("How much workers do you want to get?"))
    except:
        print("Invalid Input")
        return
    if WorkerEmployed > Assets["Space Available"]:
        print("You do not have enough properties to put that much workers in.")
        return
    WorkerEmployed2 = input("How much should each get paid? (1) Low pay/(2) Medium pay/(3) High pay").lower()
    if WorkerEmployed2 == "1":
        Workers["Low pay worker"] += WorkerEmployed
        Assets["Space Available"] -= WorkerEmployed
    elif WorkerEmployed2 == "2":
        Workers["Medium pay worker"] += WorkerEmployed
        Assets["Space Available"] -= WorkerEmployed
    elif WorkerEmployed2 == "3":
        Workers["High pay worker"] += WorkerEmployed
        Assets["Space Available"] -= WorkerEmployed

def lawyer_expense():
    Assets["Money"] -= (Lawyers["Protection"] * 2000)
    Assets["Money"] -= (Lawyers["Financial"] * 1000)
    Assets["Money"] -= (Lawyers["Property"] * 500)
def LawyerBuy():
    print("""You want lawyers. Prices per lawyer (every paycheck/cycle):
    (1) Financial: 10000
    (2) Property: 5000
    (3) Protection: 20000
    Type '0' to cancel.
    """)

    LawyerChoice = input("Which lawyer do you want? ").lower()
    if LawyerChoice == "0":
        return

    if LawyerChoice == "1":
        cost = 10000
        key = "Financial"
    elif LawyerChoice == "2":
        cost = 5000
        key = "Property"
    elif LawyerChoice == "3":
        cost = 20000
        key = "Protection"
    else:
        print("Invalid lawyer type.")
        return

    try:
        amount = int(input("How many do you want to buy? "))
        if amount <= 0:
            print("Invalid amount.")
            return
    except:
        print("Invalid input.")
        return

    total_cost = cost * amount

    if Assets["Money"] < total_cost:
        print("You can't afford that many lawyers.")
        print("Needed:", total_cost, "Available:", Assets["Money"])
        return

    Assets["Money"] -= total_cost
    Lawyers[key] += amount


def Chaos():
    if ChaosEvent == True:
        ChaosChoice = random.randint(1, ChaosEventChance)
        if ChaosChoice == 1:
            if Assets["Money"] > 1000000000:
                ChaosGenerator = random.randint(1, 20)
            elif Assets["Money"] > 100000000:
                ChaosGenerator = random.randint(1, 17)
            elif Assets["Money"] > 10000:
                ChaosGenerator = random.randint(1, 13)
            else:
                ChaosGenerator = random.randint(1, 6)

            if ChaosGenerator == 1:
                print("You won the lottery")
                Assets["Money"] += random.randint(100, 1000)
            elif ChaosGenerator == 2:
                print("You won a Studio!")
                Upgrade["Studio"] += 1
            elif ChaosGenerator == 3:
                print("You got mugged")
                Assets["Money"] -= random.randint(1, 100)
            elif ChaosGenerator == 4:
                amountwin = random.randint(1, 5)
                print("You won", amountwin, "buttcoin.")
                Assets["Butt Coin"] += amountwin
            elif ChaosGenerator == 5:
                print("You hear wise advice from an old man... Never get into debt kid")
            elif ChaosGenerator == 6:
                print("You pick up 10 dollars from the street, Lucky!")
                Assets["Money"] += 10
            elif ChaosGenerator == 7:
                Assets["Money"] -= 500
                print("A factory of yours exploded you got filed 10 lawsuits from family of dead workers")
                if Lawyers["Protection"] > 0:
                    print("LAWSUIT")
                    if Lawyers["Protection"] > 7:
                        Revenge = input("You won the lawsuit, do you want to let the families off, or do you want to charge them 100 each? (1) Yes/(2) No")
                        if Revenge == 1:
                            print("YOU WON AND CHARGED THE FAMILIES 100 EACH!")
                            Assets["Money"] += 1000
                        else:
                            print("You let them off")


                    else:
                        print("You got charged 500")
                else:
                    print("You got charged 500")
            elif ChaosGenerator == 8:
                ButtCoin = 1
                print("BUTTCOIN SERVERS HACKED, EVERYONE WHO HAD BUTTCOIN JUST LOST 100")
                if Assets["Butt Coin"] >= 100:
                    Assets["Butt Coin"] -= 100
                elif Assets["Butt Coin"] > 0:
                    Assets["Butt Coin"] = 0
                else:
                    print("Thank Gosh, you had no buttcoin")
            elif ChaosGenerator == 9:
                print("You got a taxed 4% of all of your money (1) yes/ (2) no")
                if Lawyers["Financial"] > 0:
                    Avoidance = input("Do you want to avoid the tax by sending it offshore?").lower()
                    if Avoidance == "1":
                        print("Your financial laywer sent your money to an off shore account to avoid the tax")
                        Assets["Company_Karma"] -= 30
                    else:
                        Assets["Money"] -= Assets["Money"] * 0.04

                else:
                    Assets["Money"] -= Assets["Money"] * 0.04
            elif ChaosGenerator == 10:
                print("TRADING HALT! All economic activity has been temporarily suspended.")
                time.sleep(random.randint(30, 50))
                print("The trading shall continue")
            elif ChaosGenerator == 11:
                Assets["Money"] = Assets["Money"] + (Assets["Money"] * 20 // 100)
                print("Stock Price up by 20%!")
            elif ChaosGenerator == 12:
                if Assets["Company_Karma"] < -300:
                    print("Your Stock crashed by 50%")
                    Assets["Money"] = Assets["Money"] // 2
                else:
                    print("You bought a new car")
                    Assets["Money"] -= 1000

            elif ChaosGenerator == 13:
                print("You've been sued by a rival company")
                if Lawyers["Protection"] > 0:
                    Enemy1 = random.randint(1, 10)
                    if Lawyers["Protection"] >= Enemy1:
                        print("You won the lawsuit")
                        Win1 = random.randint(1000, 5000)
                        print("You won the lawsuit and got", Win1, "dollars.")
                        Assets["Money"] += Win1
                    else:
                        Win1 = random.randint(1000, 10000)
                        print("You lost the lawsuit and lost", Win1, "dollars.")
                        Assets["Money"] -= Win1
                else:
                    Win1 = random.randint(1000, 10000)
                    print("You lost the lawsuit and lost", Win1, "dollars.")
                    Assets["Money"] -= Win1
            elif ChaosGenerator == 14:
                print("People hate you, because your rich...")
                Assets["Company_Karma"] -= 100
            elif ChaosGenerator == 15:
                print("You've been sued by a rival company")
                if Lawyers["Protection"] > 0:
                    Enemy2 = random.randint(30, 50)
                    if Lawyers["Protection"] >= Enemy2:
                        print("You won the lawsuit")
                        Win2 = random.randint(10000, 50000)
                        print("You won the lawsuit and got", Win2, "dollars.")
                        Assets["Money"] += Win2
                    else:
                        Win2 = random.randint(10000, 100000)
                        print("You lost the lawsuit and lost", Win2, "dollars.")
                        Assets["Money"] -= Win2
                else:
                    Win2 = random.randint(1000, 10000)
                    print("You lost the lawsuit and lost", Win2, "dollars.")
                    Assets["Money"] -= Win2
            elif ChaosGenerator == 16:
                if Assets["Company_Karma"] < -500:
                    print("BUSINESS IS BUSINESS AND BUSINESS MUST GROW!")
                    Assets["Money"] += 5000000
                else:
                    print("Business is pretty stale right now.")
            elif ChaosGenerator == 17:
                if Assets["Company_Karma"] < -700:
                    print("MONEY COMES MONEY GOES!")
                    Assets["Money"] += random.randint(-5000000, 5000000)
                else:
                    print("Business is pretty stale right now.")
            elif ChaosGenerator == 18:
                print("You've been sued by a rival company")
                if Lawyers["Protection"] > 0:
                    Enemy3 = random.randint(300, 500)
                    if Lawyers["Protection"] >= Enemy3:
                        print("You won the lawsuit")
                        Win3 = random.randint(100000000, 500000000)
                        print("You won the lawsuit and got", Win3, "dollars.")
                        Assets["Money"] += Win3
                    else:
                        Win3 = random.randint(100000000, 500000000)
                        print("You lost the lawsuit and lost", Win3, "dollars.")
                        Assets["Money"] -= Win3
                else:
                    Win3 = random.randint(10000000, 1000000000)
                    print("You lost the lawsuit and lost", Win3, "dollars.")
                    Assets["Money"] -= Win3
            elif ChaosGenerator == 19:
                print("BOOST IN PROFITS!")
                Assets["Money"] += random.randint(10000000, 50000000)
            elif ChaosGenerator == 20:
                print("The Public Hates you more because your a billionare")
                Assets["Company_Karma"] -= 500
        else:
            print("The wind blows on your hair")




def Sell_Discorveries():
    Assets["Money"] -= 500
    Audiencetopbid = random.randint(1, 500)
    print("You have", Assets["Discoveries"],"discoveries.")
    Sale = int(input("How much do you want to start the bid at?"))
    if Sale > Audiencetopbid:
        print("You started the bid for each too big")
    else:
        print("The Audience top bid was", Audiencetopbid)
        Assets["Money"] += (Audiencetopbid * Assets["Discoveries"])
        Assets["Discoveries"] = 0
def Market_Comments():
    if Assets["Company_Karma"] >= 0:
        if Assets["Company_Karma"] >= 30:
            if Assets["Company_Karma"] >= 5000:
                if Assets["Company_Karma"] >= 5000000:
                    Comment2 = random.randint(1, 8)
                    if Comment2 == 1:
                        print("Business extremely popular")
                    elif Comment2 == 2:
                        print("Hey calling here just to tell you that you guys are doing AMAZING! WE LOVE YOU")
                    elif Comment2 == 3:
                        print("You guys are peak!")
                    elif Comment2 == 4:
                        ButtCoinAnswer = input(
                            "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                        if ButtCoinAnswer == "1":
                            print("ButtCoin is currently", ButtCoin, "dollars.")
                            ButtCoinAmount = int(input(
                                "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                            Assets["Money"] -= ButtCoinAmount * ButtCoin
                            Assets["Butt Coin"] += ButtCoinAmount
                        else:
                            print("Well here's my number! 57+ ############")
                    elif Comment2 == 5:
                        print("I just wanted... to ask... how much do you pay your pr team liar...")
                    elif Comment2 == 6:
                        ButtCoinAnswer = input(
                            "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                        if ButtCoinAnswer == "1":
                            print("ButtCoin is currently", ButtCoin, "dollars.")
                            ButtCoinAmount = int(input(
                                "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                            Assets["Money"] -= ButtCoinAmount * ButtCoin
                            Assets["Butt Coin"] += ButtCoinAmount
                        else:
                            print("Well here's my number! 57+ ############")
                    elif Comment2 == 7:
                        print("5 stars out of 5, perfection")
                    elif Comment2 == 8:
                        print("LOVE YOU!")

                else:
                    Comment2 = random.randint(1, 8)
                    if Comment2 == 1:
                        print("Business thriving with customers")
                    elif Comment2 == 2:
                        print("Hey calling here just to tell you that you guys are doing really good!")
                    elif Comment2 == 3:
                        print("You guys are great!")
                    elif Comment2 == 4:
                        ButtCoinAnswer = input(
                            "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                        if ButtCoinAnswer == "1":
                            print("ButtCoin is currently", ButtCoin, "dollars.")
                            ButtCoinAmount = int(input(
                                "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                            Assets["Money"] -= ButtCoinAmount * ButtCoin
                            Assets["Butt Coin"] += ButtCoinAmount
                        else:
                            print("Well here's my number! 57+ ############")
                    elif Comment2 == 5:
                        print("I'm calling for a refund")
                    elif Comment2 == 6:
                        ButtCoinAnswer = input(
                            "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                        if ButtCoinAnswer == "1":
                            print("ButtCoin is currently", ButtCoin, "dollars.")
                            ButtCoinAmount = int(input(
                                "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                            Assets["Money"] -= ButtCoinAmount * ButtCoin
                            Assets["Butt Coin"] += ButtCoinAmount
                        else:
                            print("Well here's my number! 57+ ############")
                    elif Comment2 == 7:
                        print("4 stars out of 5, good")
                    elif Comment2 == 8:
                        print("really good")

            else:
                Comment2 = random.randint(1, 8)
                if Comment2 == 1:
                    print("Local Business has become more popular.")
                elif Comment2 == 2:
                    print("Hey calling here just to tell you that you guys are doing good!")
                elif Comment2 == 3:
                    print("My car crashed into one of your generators, I demand insurance.")
                elif Comment2 == 4:
                    ButtCoinAnswer = input(
                        "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                    if ButtCoinAnswer == "1":
                        print("ButtCoin is currently", ButtCoin, "dollars.")
                        ButtCoinAmount = int(input(
                            "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                        Assets["Money"] -= ButtCoinAmount * ButtCoin
                        Assets["Butt Coin"] += ButtCoinAmount
                    else:
                        print("I highly recommend you reconsider my friend, but fine.")
                elif Comment2 == 5:
                    print("I'm calling for a refund")
                elif Comment2 == 6:
                    ButtCoinAnswer = input(
                        "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                    if ButtCoinAnswer == "1":
                        print("ButtCoin is currently", ButtCoin, "dollars.")
                        ButtCoinAmount = int(input(
                            "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                        Assets["Money"] -= ButtCoinAmount * ButtCoin
                        Assets["Butt Coin"] += ButtCoinAmount
                    else:
                        print("I highly recommend you reconsider my friend, but fine.")
                elif Comment2 == 7:
                    print("4 stars out of 5, good")
                elif Comment2 == 8:
                    print("1 out of 5, I regret ever seeing your company")
        else:
            Comment1 = random.randint(1, 4)
            print("Checking reputation and comments...")
            time.sleep(random.randint(1, 2))
            if Comment1 == 1:
                print("You guys exist?")
            elif Comment1 == 2:
                print("cool... I guess")
            elif Comment1 == 3:
                print("New Business just opened up South East something something...")
            elif Comment1 == 4:
                print("Hey I'm calling here for the get two buy 1 discount? Can I only buy the free 1?")


    elif Assets["Company_Karma"] < 0:
        if Assets["Company_Karma"] < -5000:
            if Assets["Company_Karma"] < -500000:
                Comment6 = random.randint(1, 16)
                if Comment6 == 1:
                    print("YOU SUCK!!! STOP RUINING THE WORLD!!!!")
                elif Comment6 == 2:
                    print("1 out of 5 stars, COMPLETE SCAM")
                elif Comment6 == 3:
                    print("YOUR A GREEDY FAILURE")
                elif Comment6 == 4:
                    print("I LOVE YOUR PRODUCTS")
                elif Comment6 == 5:
                    print("Company has rapid growth due to abuse of nature")
                elif Comment6 == 6:
                    ButtCoinAnswer = input(
                        "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                    if ButtCoinAnswer == "1":
                        print("ButtCoin is currently", ButtCoin, "dollars.")
                        ButtCoinAmount = int(input(
                            "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                        Assets["Money"] -= ButtCoinAmount * ButtCoin
                        Assets["Butt Coin"] += ButtCoinAmount
                    else:
                        print("Hmm, knew someone shady clearly wouldn't buy the hottest thing in town")
                elif Comment6 == 7:
                    print("Climate FootPrint is blah blah blah")
                elif Comment6 == 8:
                    print("SUCK SUCK SUCK")
                elif Comment6 == 9:
                    ButtCoinAnswer = input(
                        "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                    if ButtCoinAnswer == "1":
                        print("ButtCoin is currently", ButtCoin, "dollars.")
                        ButtCoinAmount = int(input(
                            "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                        Assets["Money"] -= ButtCoinAmount * ButtCoin
                        Assets["Butt Coin"] += ButtCoinAmount
                    else:
                        print("Hmm, knew someone shady clearly wouldn't buy the hottest thing in town")
                elif Comment6 == 10:
                    print("You should burn in ****")
                elif Comment6 == 11:
                    print("MONEY MONEYYYYYY")
                elif Comment6 == 12:
                    print("0 stars, YOUR COMPANY SUCKS")
                elif Comment6 == 13:
                    print("2 out of 5, we expected quality")
                elif Comment6 == 14:
                    print("They know they could be better, but they'd rather have another yatch")
            else:
                Comment4 = random.randint(1, 7)
                if Comment4 == 1:
                    print("You Guys should do better")
                if Comment4 == 2:
                    print("I HATE YOU")
                if Comment4 == 3:
                    print("The world would not be worth living in without you")
                if Comment4 == 4:
                    ButtCoinAnswer = input(
                        "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                    if ButtCoinAnswer == "1":
                        print("ButtCoin is currently", ButtCoin, "dollars.")
                        ButtCoinAmount = int(input(
                            "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                        Assets["Money"] -= ButtCoinAmount * ButtCoin
                        Assets["Butt Coin"] += ButtCoinAmount
                    else:
                        print("Hmph, should have known a horrible person would have no sense")
                if Comment4 == 5:
                    print("2 out of 5")
                if Comment4 == 6:
                    print("1 out of 10")
                if Comment4 == 7:
                    ButtCoinAnswer = input(
                        "Hello I wanted to give you a business proposition to buy some buttcoin, would you like some? (1) yes/(2) no").lower()
                    if ButtCoinAnswer == "1":
                        print("ButtCoin is currently", ButtCoin, "dollars.")
                        ButtCoinAmount = int(input(
                            "Great, now how much do you want buy? (Also, trust me this is totally a legit safe investment that doesn't crash after a tweet from some billionare."))
                        Assets["Money"] -= ButtCoinAmount * ButtCoin
                        Assets["Butt Coin"] += ButtCoinAmount
                    else:
                        print("Hmph, should have known a horrible person would have no sense")


        else:
            Comment3 = random.randint(1, 4)
            if Comment3 == 1:
                print("Your such a meh company")
            if Comment3 == 2:
                print("3 out of 5")
            if Comment3 == 3:
                print("Protect the enviroment!")
            if Comment3 == 4:
                print("Fart")


def Land_Market():
    McFarmersTm = random.randint(15, 30)
    ForestCorp = random.randint(1, 10)
    GenevaCorp = random.randint(100, 300)
    BlackMarket = random.randint(1, 500)
    BlackMarketLand = random.randint(1, 10)
    print("Market:")
    print("(1) McFarmersTm:", McFarmersTm, "$ for 1 land.")
    print("(2) ForestCorp:", ForestCorp, "$ for 1 land.")
    print("(3) GenevaCorp:", GenevaCorp, "$ for 5 land.")
    print("(4) BlackMarket:", BlackMarket, "$ for", BlackMarketLand,"land.")
    Land_Bought = input("Here's the market choose what you want to buy, if you don't want to buy anything, just type 0.").lower()
    if Land_Bought == "1":
        print("You bought land from McFarmersTm! Thank Ya for your purchase, please don't sue us")
        Assets["Land Available"] += 1
        Assets["Money"] -= McFarmersTm
    elif Land_Bought == "2":
        killedtree = random.randint(70, 120)
        print("You bought land from ForestCorp! Thank you for your purchase.")
        print("You just cut down", killedtree, "trees to make room")
        if killedtree > 100:
            Law["Illegal Logging"] += (killedtree - 100)
        Assets["Land Available"] += 1
        Assets["Money"] -= ForestCorp
        Assets["Company_Karma"] -= random.randint(1, 20)
        Extras["Tree Dead"] += killedtree
    elif Land_Bought == "3":
        print("You bought land from GenevaCorp. Terms and Service Below.")
        Assets["Land Available"] += 5
        Assets["Money"] -= GenevaCorp
    elif Land_Bought == "4":
        print("...")
        Assets["Land Available"] += BlackMarketLand
        Assets["Money"] -= BlackMarket
        Law["BlackMarketBought"] += BlackMarketLand







def buy_stuff():
    Bought = input("Do you want to buy anything? (1) yes/ (2) no").lower()
    if Bought == "1":
        Property_Bought = input("""Now choose what you want to buy :
            (1) Generator: 50
            (2) Big Generator: 300
            (3) Studio: 100
            (4) Big Studio: 1000
            (5) PR Headquarter: 100
            (6) Lab: 5000
            (7) Big Lab: 10000
            (8) Space Headquarters: 50000
            (9) Rocket Ship: 10000
            (10) Space Station: 100000
            """).lower()
        BulkBuy = int(input("Now how much do you want to buy of it?"))
        if Property_Bought == "1":
            Upgrade["Generator"] += BulkBuy
            Assets["Money"] -= (50 * BulkBuy)
            Assets["Land Available"] -= BulkBuy
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "2":
            Upgrade["Big Generator"] += BulkBuy
            Assets["Money"] -= (300 * BulkBuy)
            Assets["Land Available"] -= BulkBuy
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "3":
            Upgrade["Studio"] += BulkBuy
            Assets["Money"] -= (100 * BulkBuy)
            Assets["Land Available"] -= BulkBuy
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "4":
            Upgrade["Big Studio"] += BulkBuy
            Assets["Money"] -= (1000 * BulkBuy)
            Assets["Land Available"] -= (BulkBuy * 2)
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "5":
            Upgrade["PR Headquarter"] += BulkBuy
            Assets["Money"] -= (100 * BulkBuy)
            Assets["Land Available"] -= BulkBuy
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "6":
            Upgrade["Lab"] += BulkBuy
            Assets["Money"] -= (5000 * BulkBuy)
            Assets["Land Available"] -= BulkBuy
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "7":
            Upgrade["Big Lab"] += BulkBuy
            Assets["Money"] -= (10000 * BulkBuy)
            Assets["Land Available"] -= (BulkBuy * 2)
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "8":
            Upgrade["Space Headquarters"] += BulkBuy
            Assets["Money"] -= (50000 * BulkBuy)
            Assets["Land Available"] -= (BulkBuy * 5)
            Assets["Space Available"] += (BulkBuy * 5)
        elif Property_Bought == "9":
            if Upgrade["Space Headquarters"] > 0:
                Upgrade["Rocket Ship"] += BulkBuy
                Assets["Money"] -= (10000 * BulkBuy)
                Assets["Space Available"] += (BulkBuy * 5)
            else:
                print("You don't have a space headquarter, where ya gonna launch that ship?")
        elif Property_Bought == "10":
            if Upgrade["Space Headquarters"] > 0:
                Upgrade["Space Station"] += BulkBuy
                Assets["Money"] -= (100000 * BulkBuy)
                Assets["Space Available"] += (BulkBuy * 5)
            else:
                print("You don't have a space headquarter, where ya gonna launch that ship?")








def pay_check():

    Assets["Money"] += ((Upgrade["Generator"] * 5) * ((Bonus1 + Bonus2 + Bonus3) // 3 ))
    Assets["Money"] += ((Upgrade["Big Generator"] * 10) * ((Bonus1 + Bonus2 + Bonus3) // 3))
    Assets["Money"] += ((Upgrade["Studio"] * 7) * ((Bonus1 + Bonus2 + Bonus3) // 3))
    Assets["Money"] += ((Upgrade["Big Studio"] * 15) * ((Bonus1 + Bonus2 + Bonus3) / 3))
    Assets["Discoveries"] += ((Upgrade["Lab"] * random.randint(0, 1)) * ((Bonus1 + Bonus2 + Bonus3) // 3))
    Assets["Discoveries"] += ((Upgrade["Big Lab"] * random.randint(0, 5)) * ((Bonus1 + Bonus2 + Bonus3) // 3))
    Assets["Money"] += ((Upgrade["Space Headquarters"] * 30) * ((Bonus1 + Bonus2 + Bonus3) // 3))
    Assets["Money"] += ((Upgrade["Rocket Ship"] * random.randint(0, 1000)) * ((Bonus1 + Bonus2 + Bonus3) // 3))
    Assets["Money"] += ((Upgrade["Space Station"] * 500) * ((Bonus1 + Bonus2 + Bonus3) // 3))
    Assets["Company_Karma"] += Upgrade["PR Headquarter"]
    Assets["Money"] -= Bank["Money Owed"] // 10
    Chaos()
    Tax()

    for i in range(Upgrade["PR Headquarter"]):
        PrClout()
    if Assets["Land Available"] < 0:
        Land_Owed = abs(Assets["Land Available"])
        Assets["Money"] -= Land_Owed * 50
        Land_Owed = 0


def print_stats():
    print("Money:", Assets["Money"])
    print("Land Available:", Assets["Land Available"])
    print("Discoveries", Assets["Discoveries"])
    print("Butt Coin:", Assets["Butt Coin"])
    print("Money Owed:", Bank["Money Owed"])
    if SeeKarma == True:
        print("Karma:", Assets["Company_Karma"])
    else:
        print("")



print("Welcome to the tycoonpia! Will you become rich, or will you fail as a pathetic failure in the dirt?")
Mode = "Work"
Game = True
while Game:
    Bonus1 = Workers["Low pay worker"] + 1
    Bonus2 = Workers["Medium pay worker"] + 1
    Bonus3 = Workers["High pay worker"] + 1
    ButtCoin = random.randint(1, 130)
    Work = input("What mode do you want, (1) Work or (2) Grind?").lower()
    if Work == "1":
        WorkChoice = input("""Do you want to shop for 
        (1) land, 
        (2) properties, 
        (3) check company rep, 
        (4) pay off some debt, 
        (5) hire lawyers, 
        (6) hire workers, 
        (7) Pr Control, 
        (8) sell buttcoin, 
        (9) sell discoveries,
        (10) or maybe check the shop?
        (11) Tax Evasion Toggle 
        (0) settings""").lower()
        if WorkChoice == "1":
            Land_Market()
        elif WorkChoice == "2":
            buy_stuff()
        elif WorkChoice == "3":
            Market_Comments()
        elif WorkChoice == "4":
            print("You currently owe to the bank", Bank["Money Owed"], "Adjusted to Interest Rate.")
            pay_debt = int(input("How much do you want to pay off?"))
            if pay_debt > Assets["Money"]:
                print("Invalid Input")
            elif pay_debt <= Assets["Money"]:
                Bank["Money Owed"] -= pay_debt
                Assets["Money"] -= pay_debt
                if Bank["Money Owed"] <= 0:
                    Bank["Money Owed"] = 0
                    Bank["Interest Rate"] = 0
                    BanksPacience = 5
            else:
                print("Invalid Input")
        elif WorkChoice == "8":
            if Assets["Butt Coin"] > 0:
                print("ButtCoin is currently", ButtCoin, "dollars.")
                SaleofButt = int(input("How much Butt Coin would you like to sell"))
                if SaleofButt > Assets["Butt Coin"]:
                    print("Invalid, when did we start selling stuff we didn't have?")
                elif SaleofButt <= Assets["Butt Coin"]:
                    SaleButt = SaleofButt * ButtCoin
                    Assets["Money"] += SaleButt
                    Assets["Butt Coin"] -= SaleofButt
                else:
                    print("Invalid Input")
        elif WorkChoice == "5":
            LawyerBuy()
        elif WorkChoice == "6":
            worker()
        elif WorkChoice == "9":
            Sell_Discorveries()
        elif WorkChoice == "7":
            PrLies()
        elif WorkChoice == "11":
            if Lawyers["Financial"] > 0:
                TaxEvasionControl = input("Do you want to avoid tax? (1) Yes/(2) No")
                if TaxEvasionControl == "1":
                    TaxEvasionControl = True
                else:
                    TaxEvasionControl = False
            else:
                print("You need a financial lawyer for this punk")
        elif WorkChoice == "10":
            Shopping()

        elif WorkChoice == "0":
            print("Current Settings:")
            print("(1) Chaos Event:", ChaosEvent)
            print("(2) Chaos Event Chance:", ChaosEventChance)
            print("(3) See Karma:", SeeKarma)
            print("(4) Money:", Assets["Money"])
            print("(5) Discoveries:", Assets["Discoveries"])
            print("(6) Generators:", Upgrade["Generator"])
            print("(7) Big Generators:", Upgrade["Big Generator"])
            print("(8) Studios:", Upgrade["Studio"])
            print("(9) Big Studios:", Upgrade["Big Studio"])
            print("(8) PR Headquarters:", Upgrade["PR Headquarter"])
            print("(9) Labs:", Upgrade["Lab"])
            print("(10) Big Labs:", Upgrade["Big Lab"])
            print("(11) Space Headquarters:", Upgrade["Space Headquarters"])
            print("(12) Rocket Ships:", Upgrade["Rocket Ship"])
            print("(13) Space Stations:", Upgrade["Space Station"])
            Change = input("Which setting would you like to change? If you don't say nothing").lower()
            if Change == "1":
                Choice1 = input("(1) True/(2) False").lower()
                if Choice1 == "1":
                    ChaosEvent = True
                elif Choice1 == "2":
                    ChaosEvent = False
                else:
                    print("Invalid Input")
            elif Change == "2":
                Choice2 = int(input("What do you want the chances to be 1 out of what?"))
                ChaosEventChance = Choice2
            elif Change == "3":
                Choice3 = input("(1) True/(2) False").lower()
                if Choice3 == "1":
                    SeeKarma = True
                elif Choice3 == "2":
                    SeeKarma = False
                else:
                    print("Invalid Input")


            elif Change == "4":
                Choice4 = int(input("Set Money to: "))
                Assets["Money"] = Choice4
            elif Change == "5":
                Choice5 = int(input("Set Discoveries to: "))
                Assets["Discoveries"] = Choice5


            elif Change == "6":
                Choice6 = int(input("Set Generator to: "))
                Upgrade["Generator"] = Choice6
            elif Change == "7":
                Choice7 = int(input("Set Big Generator to: "))
                Upgrade["Big Generator"] = Choice7
            elif Change == "8":
                Choice8 = int(input("Set Studio to: "))
                Upgrade["Studio"] = Choice8
            elif Change == "9":
                Choice9 = int(input("Set Big Studio to: "))
                Upgrade["Big Studio"] = Choice9
            elif Change == "10":
                Choice10 = int(input("Set PR Headquarter to: "))
                Upgrade["PR Headquarter"] = Choice10
            elif Change == "11":
                Choice11 = int(input("Set Lab level to: "))
                Upgrade["Lab"] = Choice11
            elif Change == "12":
                Choice12 = int(input("Set Big Lab to: "))
                Upgrade["Big Lab"] = Choice12
            elif Change == "13":
                Choice13 = int(input("Set Space Headquarters to: "))
                Upgrade["Space Headquarters"] = Choice13
            elif Change == "14":
                Choice14 = int(input("Set Rocket Ship to: "))
                Upgrade["Rocket Ship"] = Choice14
            elif Change == "15":
                Choice15 = int(input("Set Space Station to: "))
                Upgrade["Space Station"] = Choice15
            elif Change == "16":
                Choice16 = int(input("Set Land to: "))
                Assets["Land Available"] = Choice16

            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    elif Work == "2":
        Cycles = int(input("How much do you want to grind?"))
        for i in range(Cycles):
            print("Income Arriving... (Zero Income also possible)")
            time.sleep(3 - (Assets["GrinderBooster"] + Assets["GrinderBooster2"]))
            print("CHA CHING!")
            pay_check()
            lawyer_expense()
            WorkerPay()
            LawSystem()
            print_stats()





    else:
        print("Invalid Input")

    if Assets["Money"] < 0:

        if Assets["Money"] < 0:
            Bank["Money Owed"] += abs(Assets["Money"])
            Assets["Money"] = 0
            print("You've gone into debt! Bank collected", Bank["Money Owed"], "dollars.")
    if Bank["Money Owed"] > 0:
        Bank["Interest Rate"] += 1
        Bank["Money Owed"] += Bank["Money Owed"] * (Bank["Interest Rate"] / 100)
        Assets["Money"] -= Bank["Money Owed"] // 10
    print_stats()
    Chaos()
    if Assets["Land Available"] < 0:
        Land_Owed = abs(Assets["Land Available"])
        Assets["Money"] -= Land_Owed * 50
        Land_Owed = 0
        Assets["Land Available"] = 0
    if Assets["Money"] < -5000000:
        print("The Bank never accepted you juggling so much debt... no, no, no. You are going to jail forever my friend")
        exit()

    if Bank["Money Owed"] > ((Assets["Money"] + 50) * 5):
        if BanksPacience == 0:

            while Bank["Money Owed"] > 0 and Upgrade["Generator"] > 0:
                Bank["Money Owed"] -= 5
                Upgrade["Generator"] -= 1
                print("Generator? Sold for $5.")
                time.sleep(2)

            while Bank["Money Owed"] > 0 and Upgrade["Big Generator"] > 0:
                Bank["Money Owed"] -= 30
                Upgrade["Big Generator"] -= 1
                print("Big Generator? Sold for $30.")
                time.sleep(2)

            while Bank["Money Owed"] > 0 and Upgrade["Studio"] > 0:
                Bank["Money Owed"] -= 7
                Upgrade["Studio"] -= 1
                print("Studio? Sold for $7.")
                time.sleep(2)

            while Bank["Money Owed"] > 0 and Upgrade["Big Studio"] > 0:
                Bank["Money Owed"] -= 100
                Upgrade["Big Studio"] -= 1
                print("Studio? Sold for $100.")
                time.sleep(2)

            while Bank["Money Owed"] > 0 and Upgrade["Lab"] > 0:
                Bank["Money Owed"] -= 100
                Upgrade["Lab"] -= 1
                print("Lab? Sold for $100.")
                time.sleep(2)

            while Bank["Money Owed"] > 0 and Upgrade["Big Lab"] > 0:
                Bank["Money Owed"] -= 500
                Upgrade["Big Lab"] -= 1
                print("Big Lab? Sold for $500.")
                time.sleep(2)

            while Bank["Money Owed"] > 0 and Upgrade["Space Headquarters"] > 0:
                Bank["Money Owed"] -= 50000
                Upgrade["Space Headquarters"] -= 1
                print("Space Headquarters? Sold for $50000.")
                time.sleep(2)

            while Bank["Money Owed"] > 0 and Upgrade["Rocket Ship"] > 0:
                Bank["Money Owed"] -= 10000
                Upgrade["Rocket Ship"] -= 1
                print("Space Headquarters? Sold for $10000.")
                time.sleep(2)
            while Bank["Money Owed"] > 0 and Upgrade["Space Station"] > 0:
                Bank["Money Owed"] -= 50000
                Upgrade["Space Station"] -= 1
                print("Space Station? Sold for $50000.")
                time.sleep(2)

            if Bank["Money Owed"] > 0:
                Game = False
                print("The Bank is tired of your pathetic debt, they are cutting ties now. BANKRUPT. GAME OVER.")
            else:
                print("The Bank seized some of your assets to pay off the debt.")




        else:
            BanksPacience -= 1
            print("Warning you are in high debt, pay it back soon.")

    if Assets["Money"] > 1000000000000:
        if WeirdMessage == True:
            print("""







                    So...""")
            time.sleep(2)
            print("Your now a trillionare...")
            time.sleep(3)
            print("The way you got here, I don't know...")
            time.sleep(1)
            print("I will come back... and when I do...")
            time.sleep(5)
            print("Your life is done...")
            time.sleep(3)
            print("But don't worry, keep making money, it's the only thing your good at.")
            WeirdMessage = False
            time.sleep(5)
            print("Oh also, by the way...")
            time.sleep(3)
            print("YOUR SUED fOR 1 TRILLION DOLLARS FOR ABUSE OF POWER")
            Assets["Money"] -= 1000000000000


        else:
            print("")
        if Assets["Money"] > 100000000000000000000000000:
            print("CONGRATULATIONS yOU HAVE WON AND BECOME EXTREMELY RICH! You have now retired with your riches.")
            Game = False















