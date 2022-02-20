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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Would you like to see the data for Chicago, New York City, or Washington?').lower()
        if city not in ('chicago','new york city','washington'):
            print('Sorry! This is not listed city.')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('Would you like to filter the data for specific month or all months?').lower()
        if month not in ('all','january','february','march','april','may','june'):
            print('Sorry! This is invalid input.')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Would you like to filter the data for specific day of all days?').lower()
        if day not in ('all','saturday','sunday','monday','tuesday','wednesday','thursday','friday'):
            print('Sorry! This is invalid input.')
            continue
        else:
            break

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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name

    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        df=df[df['month']==month]

    if day != 'all':
        df=df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print ('The most common month is: ', df['month'].mode()[0], '.')

    # display the most common day of week
    print ('The most common day of week is: ', df['day_of_week'].mode()[0], '.')

    # display the most common start hour
    print ('The most common start hour is: ', df['hour'].mode()[0], '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print ('The most common start station used is: ', df['Start Station'].mode()[0], '.')

    # display most commonly used end station
    print ('The most common end station used is: ', df['End Station'].mode()[0], '.')

    # display most frequent combination of start station and end station trip
    start_and_end_stations=df.groupby(['Start Station','End Station'])
    print('The most frequent combination of start station and end station is: \n', start_and_end_stations.size().sort_values(ascending=False).head(1), '.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total trive time = ', df['Trip Duration'].sum(), ' seconds.')

    # display mean travel time
    print('Mean travel time = ', df['Trip Duration'].mean(), ' seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types: \n', df['User Type'].value_counts(), '.')

    # Display counts of gender
    if city!='washington':
        print('Counts of gender: \n', df['Gender'].value_counts(), '.')
    else:
        print('Sorry, there is no gender data for this city.')

    # Display earliest, most recent, and most common year of birth
    if city!='washington':
        print('Earliest year of birth: ', int(df['Birth Year'].min()), '.')
        print('Most recent year of birth: ', int(df['Birth Year'].max()), '.')
        print('Most common year of birth: ', int(df['Birth Year'].mode()[0]), '.')
    else:
        print('Sorry, there is no birth year data for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        rd=0
        while True:
            raw_data=input('\nWould you like to see some of the raw data? Enter Yes or No.\n').lower()
            if raw_data=='yes':
                print(df[rd:rd+5])
                rd+=5
            else:
                break
                
        restart = input('\nWould you like to restart? Enter Yes or No.\n').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
	main()
