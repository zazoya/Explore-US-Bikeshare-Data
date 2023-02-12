import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def month_fun():
    # function to get the month user want to filter with (cant work without get_filters())
    while True:
        month = input("enter name of the month you would like to filter data by (Jan,Feb,Mar,Apr,May,Jun):")
        if month.isdigit():
            print("please enter a month name not its number")
        else:
            if month.lower() == "jan" or month.lower() == "feb" or month.lower() == "mar" or month.lower() == "apr" or month.lower() == "may" or month.lower() == "jun":
                month = month.lower()

                x = {'jan': 'january',
                     'feb': 'february',
                     'mar': 'march',
                     'apr': 'april',
                     'may': 'may',
                     'jun': 'june',}
                month=x[month]
                return month
            else:
                print("this month data is not available")

def day_fun():
    #function to get the day user want to filter with (cant work without get_filters())
    while True:
        day = input("enter name of the day you would like to filter data by (St,Sn,Mn,Tu,Wn,Th,Fr):")
        if day.isdigit():
            print("please enter a day name not its number")
        else:
            if day.lower() == "st" or day.lower() == "sn" or day.lower() == "mn" or day.lower() == "tu" or day.lower() == "wn" or day.lower() == "th" or day.lower() == "fr":
                day = day.lower()
                z = {"st": "saturday",
                     "sn": "sunday",
                     "mn": "monday",
                     "tu": "tuesday",
                     "wn": "wednesday",
                     "th": "thursday",
                     "fr": "friday",}
                day = z[day]
                return day
            else:
                print("you may entered the name of the day wrong")

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.
    provide:
        type of filter the user choose
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("enter name of the city you would like to discover its data (chicago,new york city,washington):")
        if city.isdigit():
            print("please enter a valid name of city")
        else:
            if city.lower() == "chicago" or city.lower() == "new york city" or city.lower() == "washington":
                city=city.lower()
                break
            else:
                print("this city data is not available")
    # TO DO : know how the user want to filter the data
    while True:
        global yn
        yn= input("do you want to filter data by (month) or (day) or (both) or with no filter (none):").lower()
        if yn != "month" and yn != "day" and yn != "both" and yn!="none":
            print("please enter valid innput")
        else:
            if yn=="both":
                month=month_fun()
                day=day_fun()
                break
            elif yn=="month":
                month =month_fun()
                day='0'
                break
            elif yn=="day":
                day=day_fun()
                month='0'
                break
            else:
                day='0'
                month='0'
                break

    print('-' * 40)
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

    df =pd.DataFrame(pd.read_csv(CITY_DATA[city]))

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if yn=="both":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df=df[(df['month']==month) & (df['day_of_week']==day.title())]

    elif yn=="month":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month']==month]

    elif yn=="day":
        df = df[df['day_of_week']==day.title()]
    else:
        return df
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month

    months = ['January', 'February', 'March', 'April', 'May', 'June']
    x =months[df['month'].mode()[0]-1]
    y=df['month'].value_counts()[df['month'].mode()[0]]
    print("the most common month: {} -and- its count: {}".format(x,y))

    # TO DO: display the most common day of week
    a=df['day_of_week'].mode()[0]
    b=df['day_of_week'].value_counts()[a]
    print("the most common day: {} -and- its count: {} ".format(a,b))

    # TO DO: display the most common start hour
    w=df['Start Time'].dt.hour.mode()[0]
    s=df['Start Time'].dt.hour.value_counts()[w]
    print("the most common start hour: {} -and- its count: {} ".format(w,s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    a=df['Start Station'].mode()[0]
    b=df['Start Station'].value_counts()[a]
    print("the most commnly used start station: {} -and- its count: {}".format(a,b))

    # TO DO: display most commonly used end station
    a=df['End Station'].mode()[0]
    b=df['End Station'].value_counts()[a]
    print("the most commnly used end station: {} -and- its count: {}".format(a,b))
    # TO DO: display most frequent combination of start station and end station trip
    x=df.groupby(['End Station','Start Station']).size().sort_values(ascending=False).index[0]
    print("the most frequent combination of start station and end station trip: {} -And- {}".format(x[0],x[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time:",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("mean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].str.split(expand=True).stack().value_counts()
    print("counts of user types")
    print(users.to_string())
    # TO DO: Display counts of gender
    print("\n")
    if "Gender" in df:
        gender = df['Gender'].str.split(expand=True).stack().value_counts()
        print("counts of gender")
        print(gender.to_string())
    else:
        print("there is no available data about Gender in this city")
    # TO DO: Display earliest, most recent, and most common year of birth
    print("\n")
    if "Birth Year" in df:
        print("the earliest year of birth:",int(df['Birth Year'].min()))
        print("the most recent year of birth:", int(df['Birth Year'].max()))
        print("the most common year of birth:", int(df['Birth Year'].mode()))
    else:
        print("there is no available data about Birth Year in this city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rows(df):
    i=0
    while i < df.shape[0]:
        x = input("do you want to display 5 rows of data? (y/n):")
        if x.lower() == "y":
            print(df.iloc[i:i+5].to_string())
            i+=5
        elif x.lower() == "n":
            break
        else:
            print("please input a valid input")


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city,month, day)
        display_rows(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter (yes) or (no).\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
     main()