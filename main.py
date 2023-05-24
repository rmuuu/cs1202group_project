import os
class House:
    def __init__(self, area, occupants, consumption):
        self.area = area
        self.occupants = occupants
        self.consumption = consumption

    def get_base_consumption(self):
        return self.consumption

    def calculate_consumption(self, solarenergy, days, num_panels):
        base_consumption = self.get_base_consumption()
        if not solarenergy:
            return base_consumption 
        base_solarenergy = 0
        for i in range(3):
           y = solarenergy[i] * days[i]
           base_solarenergy += y
        base_solarenergy *= num_panels
        consumption = max(0, base_consumption - base_solarenergy)
        return consumption

class GeneratedEnergy:
    def __init__(self, size, hours, solarenergy):
        self.size = size
        self.hours = hours
        self.efficiency = 0.15
        self.solarenergy = solarenergy
    
    def get_generated_energy(self):
        return self.size * 1000 * self.efficiency * self.hours
        
    def final_output(self):
        return self.get_generated_energy() / 1000

class Cloudy(GeneratedEnergy):
    def __init__(self, size, hours, solarenergy):
        self.efficiency = 0.5 * 0.15 # solar panels normally generate 50 % of their optimum generation during cloudy days
        GeneratedEnergy.__init__(self, size, hours, solarenergy)

    def get_generated_energy_cloudy(self):
        return self.size * self.efficiency * self.hours

class LightRain(GeneratedEnergy):
    def __init__(self, size, hours, solarenergy):
        self.efficiency = 0.3 * 0.15 # solar panels normally generate 30 % of their optimum generation in light rain
        GeneratedEnergy.__init__(self, size, hours, solarenergy)

    def get_generated_energy_lightrain(self):
        return self.size * self.efficiency * self.hours
    
class HeavyRain(GeneratedEnergy):
    def __init__(self, size, hours, solarenergy):
        self.efficiency = 0.15 * 0.15 # solar panels normally generate 15 % of their optimum generation in heavy rain
        GeneratedEnergy.__init__(self, size, hours, solarenergy)

    def get_generated_energy_heavyrain(self):
        return self.size * self.efficiency * self.hours
    
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_duration_input(prompt):
    while True:
        duration_type = input(prompt)
        if duration_type.lower() in ['days', 'months']:
            return duration_type.lower()
        print("Invalid duration type. Please enter 'days', 'months', or 'years'.")

def get_duration_days_input(prompt, duration_type):
    while True:
        try:
            duration = input(prompt)
            if duration_type.lower() == 'days':
                return duration
            elif duration_type.lower() == 'months':
                return int(duration) * 30 # assuming there are 30 days in  a month
        except ValueError:
            print("Invalid input. Please enter a valid duration days.")

def display_energy_conservation_tips():
    print("===========================================================================")
    print("Here are some ways to conserve energy and reduce your electricity consumption:")
    print("~ Use LED light bulbs instead of traditional incandescent bulbs.")
    print("~ Turn off lights and electronics when not in use.")
    print("~ Set your thermostat a few degrees lower in the winter and a few degrees higher in the summer.")
    print("~ Wash clothes in cold water instead of hot water.")
    print("~ Use a programmable thermostat to automatically adjust the temperature when you're away from home.")
    print("~ Install weather stripping around doors and windows to prevent drafts.")
    print("~ Unplug chargers and appliances when they're not in use.")
    print("~ Plant trees or install shading devices to block the sun's rays from hitting your home.")
    print("~ Seal air leaks in your home with caulking or weather stripping.")

def header():
    print("===========================================================================")
    print("                    .__.         .___")
    print("                    |  |._ _ ._ *[__ ._  _ ._. _   .")
    print("                    |__|[ | )[ )|[___[ )(/,[  (_]\_|")
    print("                                              ._|._|")
    print("===========================================================================")


def login():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    header()
    while True:
        username = input("\nPlease enter your username: ")
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        
        password = input("Please enter your password: ")
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        
        return username, password
        

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    header()
    print("\nAbout\n\nObjectives:")
    print("\t- To determine the user's energy consumption.")
    print("\t- To calculate the generated solar energy used after solar installation.")
    print("\t- To calculate the amount of energy used after solar installation.")
    print("\t- To recommend more effective strategies to cut back on non-renewable energy use.")
    print("\nAuthors:\n\tAguilar, Rose Anne C.\n\tArenas, Aldrich Amiel A.")
    print("\tMontoya, Ram Greggor D.\n\tRecto, Nerine Rosette M.")
    
    is_logged_in = False
    while not is_logged_in:

        choice_i = input("\nPlease choose an option: \n\t1. Log in \n\t2. Exit\n\t")
        if choice_i == '1':
            username, password = login()
            is_logged_in = True
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            header()
        elif choice_i == '2':
            exit()
    
    while True:
        choice_menu = ""
        while choice_menu not in ['1', '2', '3']:
            choice_menu = input("\nPlease choose an option: \n\t1. Energy Calculator \n\t2. History \n\t3. Exit\n\t")
            if choice_menu not in ['1', '2', '3']:
              print("Invalid input. Please enter '1', '2', or '3'.")
        
        if choice_menu == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            header()

            area = get_float_input("\nEnter the area of the house in square meters: ")
            occupants = get_int_input("Enter the number of occupants in the house: ")
            consumption = get_float_input("Enter the average energy consumption of the house in kilowatt-hours: ")
            has_solar_panels = ""
            while has_solar_panels.lower() not in ['y', 'n']:
                has_solar_panels = input("Do you have solar panels installed? (y/n): ")
                if has_solar_panels.lower() not in ['y', 'n']:
                    print("Invalid input. Please enter 'Y' or 'y' or 'N' or 'n'.")
            if has_solar_panels.lower() == 'y':
                # code for when the user has solar panels
                num_panels = get_int_input("Enter the number of solar panels installed: ")
                sun_hours = get_float_input("Enter the number of sun hours in your area each day: ")
                panel_size = get_float_input("Enter the area of each solar panel in square meters: ")
                duration_type = get_duration_input("Enter the duration type (days or months): ")
                duration = get_duration_days_input(f"Enter the duration ({duration_type}): ", duration_type)
                solar_panels_hours = ["sunny", "cloudy", "rainy (light)", "rainy (heavy)"]
                days = []
                for weather in solar_panels_hours:
                    sdays = get_float_input(f"Enter the number of {weather} days in your area: ")
                    days.append(sdays)
                
                generated_energy_sun = GeneratedEnergy(panel_size, sun_hours, 0)
                generated_energy_cloudy = Cloudy(panel_size, sun_hours, 0) # assuming that it is cloudy all day
                generated_energy_lightrain = LightRain(panel_size, sun_hours, 0) # assuming that it is raining lightly all day
                generated_energy_heavyrain = HeavyRain(panel_size, sun_hours, 0) # assuming that it is raining heavily all day
                solarenergy = [generated_energy_sun.final_output(), generated_energy_cloudy.get_generated_energy_cloudy(), 
                            generated_energy_lightrain.get_generated_energy_lightrain(), generated_energy_heavyrain.get_generated_energy_heavyrain()]
                base_solarenergy = 0
                for i in range(3):
                    base_solarenergyii = solarenergy[i] * days[i]
                    base_solarenergy += base_solarenergyii
                base_solarenergy *= num_panels
                
                house = House(area, occupants, consumption)
                consumption_before = house.calculate_consumption([], days, num_panels)
                consumption_after = house.calculate_consumption(solarenergy, days, num_panels)
                
                
                savings = consumption_before - consumption_after
                
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
                header()
                print("\nThe house consumed {:.2f} kWh of electricity in {} days before installing solar panels ".format(consumption_before, duration))
                print("The installed solar panels generated {:.2f} kWh of solar energy output in {} days.". format(base_solarenergy, duration))
                print("The house consumed {:.2f} kWh of electricity in {} days after installing solar panels.".format(consumption_after, duration))
                print("The solar panels saved {:.2f} kWh of electricity in {} days.".format(savings, duration))
            
                history = open('history.txt', 'a') # history text file
                history.write("\n\nUser {}:\n".format(username))
                history.write("\n\tThe house consumed {:.2f} kWh of electricity in {} days before installing solar panels ".format(consumption_before, duration))
                history.write("\n\tThe installed solar panels generated {:.2f} kWh of solar energy output in {} days.". format(base_solarenergy, duration))
                history.write("\n\tThe house consumed {:.2f} kWh of electricity in {} days after installing solar panels.".format(consumption_after, duration))
                history.write("\n\tThe solar panels saved {:.2f} kWh of electricity in {} days.".format(savings, duration))
                history.close()

            else:
                # code for when the user doesn't have solar panels
                history = open('history.txt', 'a') # history text file
                if consumption > 100 and has_solar_panels.lower() == 'n':
                    recommended_panels = round(consumption / 50)  # assuming each panel generates 50 kWh per month
                    print("Based on your average energy consumption, we recommend installing {} solar panels.".format(recommended_panels))
                    savings = recommended_panels * 50  # assuming each panel generates 50 kWh per month
                    print("Installing these solar panels could save up to {:.2f} kWh of electricity per month.".format(savings))

                    history.write("\n\nUser {}:\n".format(username))
                    history.write("\n\tBased on your average energy consumption, we recommend installing {} solar panels.".format(recommended_panels))
                    history.write("\n\tInstalling these solar panels could save up to {:.2f} kWh of electricity per month.".format(savings))
                    history.close()
                elif consumption < 100:
                    print("Because your electric consumption is low, you just need to do the energy conservation tips to reduce your electricity consumption.")
                    display_energy_conservation_tips()
                else:
                    print("You may consider installing solar panels or follow the energy conservation tips to reduce your electricity consumption.")
                display_energy_conservation_tips()
        
        elif choice_menu == '2':
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            header()
            choice_history = ""
            while choice_history not in ['1', '2', '3']:
                choice_history = input("\nPlease choose an option: \n\t1. Show History \n\t2. Clear History \n\t3. Exit\n\t")
                if choice_history not in ['1', '2', '3']:
                    print("Invalid input. Please enter '1', '2', or '3'.")
            if choice_history == '1':
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
                history = open('history.txt', 'r') # read text file
                history_content = history.read()
                print(history_content)
                history.close()
            elif choice_history == '2':
                with open('history.txt', 'w') as history:
                    history.write("===========================================================================\n")
                    history.write("\t\t\t\t\t.__.         .___\n")
                    history.write("\t\t\t\t\t|  |._ _ ._ *[__ ._  _ ._. _   .\n")
                    history.write("\t\t\t\t\t|__|[ | )[ )|[___[ )(/,[  (_]\_|\n")
                    history.write("\t\t\t\t\t                          ._|._|\n")
                    history.write("===========================================================================\n")
                    history.write("\nHistory:")
                    history.close()
            else:
                exit()

        choice = input("\nDo you want to log out? (y/n): ")
        if choice.lower() in ['n', 'N']:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            pass
        else:
            exit()
            
if __name__ == '__main__':
    main()