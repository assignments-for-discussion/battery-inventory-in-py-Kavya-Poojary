def classify_batteries(present_capacity_list):
    
    healthy_count = 0
    exchange_count = 0
    failed_count = 0

    
    rated_capacity = 120

    for present_capacity in present_capacity_list:
        
        soh = (present_capacity / rated_capacity) * 100

        
        if soh > 80:
            healthy_count += 1
        elif 62 <= soh <= 80:
            exchange_count += 1
        else:
            failed_count += 1

    return healthy_count, exchange_count, failed_count


def test_classify_batteries():
   
    assert classify_batteries([120, 118, 115, 119, 110]) == (5, 0, 0)

    
    assert classify_batteries([95, 75, 105, 60, 85]) == (2, 2, 1)

   
    assert classify_batteries([50, 55, 58, 60, 42]) == (0, 0, 5)

    print("All tests pass.")


test_classify_batteries()
