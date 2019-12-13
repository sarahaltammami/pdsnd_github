import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.


    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Kindly input a city name:').lower()
    while 1:
        if city in CITY_DATA :
            break;
        city = input('Please choose one of the three cities').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('kindly specify a month:').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('kindly specify a day:').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)
    print("is the most common month")

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)
    print("is the most common day of the week")

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print(common_start_hour)
    print("is the most common start hour")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)
    print("is the most commonly used start station in this city")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)
    print("is the most commonly used end station in this city")

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print(str(frequent_combination)+"is the most frequent combination")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print( str(total_travel_time))
    print("is the total travel time")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(str(mean_travel_time))
    print("is the mean travel time")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(str(user_types))
    print("is the count of user types")


    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print(str(gender))
        print("Is the count of user gender")


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print(earliest_birth)
        print("is the earliest birth")
        mrb= df['Birth Year'].max()
        print(mrb)
        print("is the most recent birth")
        mcb = df['Birth Year'].mode()[0]
        print(mcb)
        print("is the most common birth: {}\n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    counter = 5
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        #Raw data
        question = input("\nDo you like to see more data? Type yes or no.\n")
        while question=='yes':
            print(df.head(counter))
            counter+=5;
            question= input('\nDo you like to see more? Type yes or no.\n')
            if question=='no':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
