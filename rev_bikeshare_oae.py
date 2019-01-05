import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print("\nHello! Let\'s explore some US bikeshare data for three major"
          " cities in the U.S.!")
    while True:
        # get user input for city (chicago, new york city, washinton)
        city = input("\nWould you like to see data for Chicago, New York or "
                     "Washington?\n").strip().lower()
        if city not in ('chicago', 'new york', 'washington'):
            print(city.title() + " is not one of the three cities...")
            continue
        else:
            break

    while True:
        # get user input for month (all, January, February,....,June)
        month = input("\nWhich month? January, February, March, April, May, "
                      "June, or All?\n").strip().lower()
        if month not in ('january', 'february', 'march', 'april', 'may',
                         'june', 'all'):
            print(month.title() + " is not one of the prescribed months...")
            continue
        else:
            break

    while True:
        # get user input for day of week (All, Monday, Tuesday,....Sunday)
        day = input("\nWhich day? Sunday, Monday, Tuesday, Wednesday,"
                    " Thursday, Friday, Saturday or All ?\n").strip().lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
                       'friday', 'saturday', 'all'):
            print(day.title() + " is not one of the days of the week...")
            continue
        else:
            break
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if
    applicable

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply
        no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('-'*50)
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print("\nThe most popular month for travelling is ", popular_month)

    # Display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("\nThe most popular day for travelling is ", popular_day_of_week)

    # Display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("\nThe most popular hour to start travelling is ", popular_hour)

    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...")
    start_time = time.time()

    # Display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print("\nThe most popular start station is ", popular_start)

    # Display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print("\nThe most popular end station is ", popular_end)

    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Statistics...")
    start_time = time.time()

    # Display total travel time
    trip_total = df['Trip Duration'].sum()
    print("\nThe total travelling time is ", trip_total)

    # Display mean travel time
    trip_ave = df['Trip Duration'].mean()
    print("\nThe average time spent on each trip is ", trip_ave)

    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare userss"""

    print("\nCalculating Bikeshare User Statistics...")
    start_time = time.time()

    # Display counts of user types
    print("\nThe breakdown of users is:\n")
    user_types = df['User Type'].value_counts()

    print(user_types)

    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*50)


def raw_data(df):
    """ Displays 5 rows of raw data at a time """
    line_number = 0
    prompt = "\n Do you want to see the raw data? Enter yes or no. \n "
    raw_input = input(prompt).strip().lower()
    if raw_input not in ('yes', 'no'):
        print(raw_input.title() + " not one of the responses")
    elif raw_input == 'no':
        return
    elif raw_input == 'yes':
        while True:
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            keep_printing = input("\nDo you want to see more raw data? "
                                  "Enter yes or no?\n ").strip().lower()
            if keep_printing not in ('yes', 'no'):
                print(keep_printing.title() + " not one of the responses")
            elif keep_printing == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
