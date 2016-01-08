from utilities.constants import QUALITY_MEASURE, EASE_MEASURE, STATUS


keys = ['User_Rating', 'Timeliness', 'Product_Quality', 'Ease_of_Deliverability', 'Quality_of_Deliveribility', 'Logistics_Cost']


def normalize(feedback):  # normalize the feedback attributes to (0,1)

    try:
        user_rating = feedback[0]  # rating from 1 to 5
        user_rating = (user_rating - 1)/(5-1)

        timeliness = feedback[1]  # time in hours (float) where 0 is the estimated time of delivery, +ve is late, -ve is early
        timeliness = max(timeliness, 0)  # because any time before estimated is satisfactory
        timeliness = timeliness/48
        timeliness = 1 - timeliness  # because later the delivery, worse it is

        quality_attributes_len = len(QUALITY_MEASURE)
        product_quality = feedback[2]  # QUALITY_MEASURE = ['Horrible', 'Extremely Poor', 'Poor', 'Average', 'Good', 'Very Good', 'Excellent']
        product_quality = QUALITY_MEASURE.index(product_quality)
        product_quality = product_quality/(quality_attributes_len - 1)

        ease_attributes_len  = len(EASE_MEASURE)
        ease_of_deliverability = feedback[3]  # EASE_MEASURE = ['Easy', 'Medium', 'Hard']
        ease_of_deliverability = EASE_MEASURE.index(ease_of_deliverability)
        ease_of_deliverability = ease_of_deliverability/(ease_attributes_len - 1)
        ease_of_deliverability = 1 - ease_of_deliverability

        delivery_quality = feedback[4]
        delivery_quality = QUALITY_MEASURE.index(delivery_quality)
        delivery_quality = delivery_quality/(quality_attributes_len - 1)


        logistics_cost = feedback[5]   # in rupees
        logistics_cost = logistics_cost/30000

        status = feedback[6]  # STATUS = ['SUCCESS', 'FAILURE']
        status = STATUS.index(status)

        feedback = [user_rating, timeliness, product_quality, ease_of_deliverability, delivery_quality, logistics_cost, status, feedback[7]]
        return feedback

    except: print 'Invalid Feedback Format'


def crunch(feedback):

    feedback = normalize(feedback)
    features = feedback[:6]
    label = feedback[6]
    return (features, label)


