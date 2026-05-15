"""
3. Create a new Python file named time_travelers_toolkit.py. This script will serve as the main program where you will combine all the elements of the project.
4. At the beginning of your script, import the necessary modules. This includes importing the datetime module with an alias of dt, Decimal from the decimal module, and the randint and choice functions from the random module. Also, import the custom_module.py you created earlier, making sure it is in the same directory as time_travelers_toolkit.py.
5. Use the datetime module to retrieve the current date and time. You’ll need to obtain both the date and the exact time at the moment the script is run.
6. Once you’ve retrieved the current date and time, print them out to the console in a clear and readable format. This will give you a reference point for when the time travel message is generated.
7. To calculate the cost of time travel, use the decimal module, which provides a way to perform precise financial calculations. First, create a base cost as a Decimal object. Then, determine a cost multiplier based on the difference between the current year and the target year. Combine these values to calculate the final cost.
8. Ensure that the final cost is formatted to two decimal places before it’s used in the time travel message.
9. Use the randint() function to generate a random year within a specified range. This random year will be the target year for the time travel.
10. Create a list of possible destinations for the time travel. Then, use the choice() function to randomly select one destination from the list.
11. After generating a random year, selecting a destination, and calculating the cost, use these values as arguments for the generate_time_travel_message() function you imported from custom_module.py earlier. Print the generated message to describe the user’s time travel experience, and congratulations on a project completed!
"""
import datetime as dt
from decimal import Decimal
from random import randint, choice

from custom_module import generate_time_travel_message


def main() -> None:
    """Generate and print a random time-travel message with cost info."""

    now = dt.datetime.now()
    current_time = now.time()
    current_date = now.date()
    current_year = current_date.year

    # avoid leading-zero integer literal (invalid in Python 3)
    target_year = randint(0, 9999)

    base_cost = Decimal('1000.00')
    multiplier = Decimal('10.00')
    years_difference = abs(target_year - current_year)
    final_cost = base_cost + (Decimal(years_difference) * multiplier)
    # ensure two decimal places
    final_cost = final_cost.quantize(Decimal('0.00'))

    destinations_list = ['Vietnam', 'UAE', 'Australia', 'Canada', 'US', 'France', 'Finland']
    destination = choice(destinations_list)

    message = generate_time_travel_message(
        target_year,
        destination,
        final_cost,
    )

    print(f"Current time: {current_time:%H:%M:%S}")
    print(f"Current date: {current_date:%B %d, %Y}")
    print(f"Target year: {target_year}")
    print(f"Traveling {years_difference} years cost: ${final_cost:.2f}")
    print(message)


if __name__ == '__main__':
    main()


