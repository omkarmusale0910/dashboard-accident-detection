import requests

# Enter your Google Maps API key here
API_KEY = "YOUR_API_KEY"

# Enter the latitude and longitude of the location you want to search from
LATITUDE = "37.7749"
LONGITUDE = "-122.4194"

# Set the type of place you want to search for (in this case, a hospital)
PLACE_TYPE = "hospital"



# Set the radius for the search (in meters)
RADIUS = 5000

# Define the API endpoint and parameters for the Nearby Search request
NEARBY_SEARCH_ENDPOINT = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
nearby_search_params = {
    "location": f"{LATITUDE},{LONGITUDE}",
    "radius": RADIUS,
    "type": PLACE_TYPE,
    "key": API_KEY
}

# Send the Nearby Search API request
nearby_search_response = requests.get(NEARBY_SEARCH_ENDPOINT, params=nearby_search_params)
nearby_search_data = nearby_search_response.json()

# Extract the Place ID of the nearest hospital
place_id = nearby_search_data["results"][0]["place_id"]

# Define the API endpoint and parameters for the Place Details request
PLACE_DETAILS_ENDPOINT = "https://maps.googleapis.com/maps/api/place/details/json"
place_details_params = {
    "place_id": place_id,
    "fields": "name,formatted_address,formatted_phone_number,website",
    "key": API_KEY
}

# Send the Place Details API request
place_details_response = requests.get(PLACE_DETAILS_ENDPOINT, params=place_details_params)
place_details_data = place_details_response.json()

# Extract the phone number and website URL of the nearest hospital
phone_number = place_details_data["result"].get("formatted_phone_number", "Phone number not available")
website = place_details_data["result"].get("website", "Website not available")

# Print the phone number and website URL of the nearest hospital
print(f"Phone number: {phone_number}")
print(f"Website: {website}")



# -----------------------------------------------------------------------------------------
import pytz
def unix_to_local(unix_timestamp, timezone):
    utc_time = datetime.utcfromtimestamp(unix_timestamp)
    utc_time = pytz.utc.localize(utc_time)
    local_time = utc_time.astimezone(pytz.timezone(timezone))
    return local_time.replace(tzinfo=None)

ct=0




# -------------------------------------------------------------------------------------------------------------------------------------------------

def get_summary_date(user_id: str, event_start_time, event_end_time, time_zone, use_dev_env: bool):
    SLEEP_BEGIN_FILTER_OFFSET = config.get('SLEEP_BEGIN_FILTER_OFFSET')
    SLEEP_END_FILTER_OFFSET = config.get('SLEEP_END_FILTER_OFFSET')

    summary_day_ts = (None, None)

    day_start_time = get_start_time(event_end_time, time_zone, 0)

    sleep_tracking_inputs = get_user_sleep_tracking_inputs(user_id, use_dev_env)

    set_wake_time = sleep_tracking_inputs.get('setWakeTime')
    set_bed_time = sleep_tracking_inputs.get('setBedTime')

    set_wake_time = day_start_time + convert_dict_to_sec(set_wake_time)
    set_bed_time = day_start_time + convert_dict_to_sec(set_bed_time)

    sleep_end_sbt_offset = SLEEP_END_FILTER_OFFSET.get('setBedTime')
    sleep_end_swt_offset = SLEEP_END_FILTER_OFFSET.get('setWakeTime')

    end_sbt = set_bed_time + convert_dict_to_sec(sleep_end_sbt_offset)
    end_swt = set_wake_time +convert_dict_to_sec(sleep_end_swt_offset)

    if end_swt <= end_sbt:
        end_swt += SECONDS_IN_DAY
        set_wake_time += SECONDS_IN_DAY

    if end_sbt < event_end_time < end_swt:
        return (set_bed_time, set_wake_time)

    end_sbt_prev_day = end_sbt - SECONDS_IN_DAY
    end_swt_prev_day = end_swt - SECONDS_IN_DAY

    if end_sbt_prev_day < event_end_time < end_swt_prev_day:        
        return (set_bed_time - SECONDS_IN_DAY, set_wake_time - SECONDS_IN_DAY)

    end_sbt_next_day = end_sbt + SECONDS_IN_DAY
    end_swt_next_day = end_swt + SECONDS_IN_DAY

    if end_sbt_next_day < event_end_time < end_swt_next_day:
        return (set_bed_time + SECONDS_IN_DAY, set_wake_time + SECONDS_IN_DAY)


    set_wake_time = sleep_tracking_inputs.get('setWakeTime')
    set_bed_time = sleep_tracking_inputs.get('setBedTime')

    set_wake_time = day_start_time + convert_dict_to_sec(set_wake_time)
    set_bed_time = day_start_time +convert_dict_to_sec(set_bed_time)
    
    sleep_begin_sbt_offset = SLEEP_BEGIN_FILTER_OFFSET.get('setBedTime')
    sleep_begin_swt_offset = SLEEP_BEGIN_FILTER_OFFSET.get('setWakeTime')

    begin_sbt = set_bed_time + convert_dict_to_sec(sleep_begin_sbt_offset)
    begin_swt = set_wake_time +convert_dict_to_sec(sleep_begin_swt_offset)

    if begin_swt <= begin_sbt:
        begin_swt += SECONDS_IN_DAY
        set_wake_time += SECONDS_IN_DAY

    if begin_sbt < event_start_time < begin_swt:
        return (set_bed_time, set_wake_time)

    begin_sbt_prev_day = begin_sbt - SECONDS_IN_DAY
    bgein_swt_prev_day = begin_swt - SECONDS_IN_DAY

    if begin_sbt_prev_day < event_start_time < bgein_swt_prev_day:
        return (set_bed_time - SECONDS_IN_DAY, set_wake_time - SECONDS_IN_DAY)

    begin_sbt_next_day = end_sbt + SECONDS_IN_DAY
    begin_swt_next_day = end_swt + SECONDS_IN_DAY

    if begin_sbt_next_day < event_start_time < begin_swt_next_day:
        return (set_bed_time + SECONDS_IN_DAY, set_wake_time + SECONDS_IN_DAY)

    return summary_day_ts



# ------------------------------------------------------------------------------------------------------------------------------------------------------


def get_summary_date(user_id: str, event_start_time, event_end_time, time_zone, use_dev_env: bool):
    SLEEP_BEGIN_FILTER_OFFSET = config.get('SLEEP_BEGIN_FILTER_OFFSET')
    SLEEP_END_FILTER_OFFSET = config.get('SLEEP_END_FILTER_OFFSET')

    summary_day_ts = (None, None)

    day_start_time = get_start_time(event_end_time, time_zone, 0)

    sleep_tracking_inputs = get_user_sleep_tracking_inputs(user_id, use_dev_env)

    # set_wake_time = sleep_tracking_inputs.get('setWakeTime')
    # set_bed_time = sleep_tracking_inputs.get('setBedTime')

    # set_wake_time = day_start_time + convert_dict_to_sec(set_wake_time)
    # set_bed_time = day_start_time + convert_dict_to_sec(set_bed_time)

    # sleep_end_sbt_offset = SLEEP_END_FILTER_OFFSET.get('setBedTime')
    # sleep_end_swt_offset = SLEEP_END_FILTER_OFFSET.get('setWakeTime')

    # end_sbt = set_bed_time + convert_dict_to_sec(sleep_end_sbt_offset)
    # end_swt = set_wake_time +convert_dict_to_sec(sleep_end_swt_offset)
    set_bed_time,set_wake_time,end_sbt,end_swt=get_sleep_window_start_end_and_window_with_offset(sleep_tracking_inputs,day_start_time,SLEEP_END_FILTER_OFFSET)

    if end_swt <= end_sbt:
        end_swt += SECONDS_IN_DAY
        set_wake_time += SECONDS_IN_DAY

    if end_sbt < event_end_time < end_swt:
        return (set_bed_time, set_wake_time)

    end_sbt_prev_day = end_sbt - SECONDS_IN_DAY
    end_swt_prev_day = end_swt - SECONDS_IN_DAY

    if end_sbt_prev_day < event_end_time < end_swt_prev_day:        
        return (set_bed_time - SECONDS_IN_DAY, set_wake_time - SECONDS_IN_DAY)

    end_sbt_next_day = end_sbt + SECONDS_IN_DAY
    end_swt_next_day = end_swt + SECONDS_IN_DAY

    if end_sbt_next_day < event_end_time < end_swt_next_day:
        return (set_bed_time + SECONDS_IN_DAY, set_wake_time + SECONDS_IN_DAY)


    # set_wake_time = sleep_tracking_inputs.get('setWakeTime')
    # set_bed_time = sleep_tracking_inputs.get('setBedTime')

    # set_wake_time = day_start_time + convert_dict_to_sec(set_wake_time)
    # set_bed_time = day_start_time +convert_dict_to_sec(set_bed_time)
    
    # sleep_begin_sbt_offset = SLEEP_BEGIN_FILTER_OFFSET.get('setBedTime')
    # sleep_begin_swt_offset = SLEEP_BEGIN_FILTER_OFFSET.get('setWakeTime')

    # begin_sbt = set_bed_time + convert_dict_to_sec(sleep_begin_sbt_offset)
    # begin_swt = set_wake_time +convert_dict_to_sec(sleep_begin_swt_offset)
    set_bed_time,set_wake_time,begin_sbt,begin_swt=get_sleep_window_start_end_and_window_with_offset(sleep_tracking_inputs,day_start_time,SLEEP_BEGIN_FILTER_OFFSET)

    if begin_swt <= begin_sbt:
        begin_swt += SECONDS_IN_DAY
        set_wake_time += SECONDS_IN_DAY

    if begin_sbt < event_start_time < begin_swt:
        return (set_bed_time, set_wake_time)

    begin_sbt_prev_day = begin_sbt - SECONDS_IN_DAY
    bgein_swt_prev_day = begin_swt - SECONDS_IN_DAY

    if begin_sbt_prev_day < event_start_time < bgein_swt_prev_day:
        return (set_bed_time - SECONDS_IN_DAY, set_wake_time - SECONDS_IN_DAY)

    begin_sbt_next_day = end_sbt + SECONDS_IN_DAY
    begin_swt_next_day = end_swt + SECONDS_IN_DAY

    if begin_sbt_next_day < event_start_time < begin_swt_next_day:
        return (set_bed_time + SECONDS_IN_DAY, set_wake_time + SECONDS_IN_DAY)

    return summary_day_ts