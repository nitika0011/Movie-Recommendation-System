# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        ##Strip all whitespaces from strings
        field_names= adapter.field_names()
        
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                adapter[field_name]=value[0].strip()
                
        ##Category & Product Type --> Switch to lowercase
        lowercase_keys =["category","product_type"]
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key]=value.lower()
            
        ##Price --> Convert to float
        price_keys = ["price_excl_tax","price_incl_tax","tax","price"]
        for price_key in price_keys:
            value=adapter.get(price_key)
            value=value.replace('£', '')
            adapter[price_key]= float(value)
            
        ##Availaibility --> extract number of books in stock
        availaibility_string = adapter.get("Availability")
        split_string_array=availaibility_string.split('(')
        if len(split_string_array)<2:
            adapter["Availability"]=0
        else:
            availaibility_array = split_string_array[1].split(' ')
            adapter["Availability"]= int(availaibility_array[0])
            
        ##Reviews --> Convert string to number
        num_reviews_string = adapter.get("No_of_reviews")
        adapter["No_of_reviews"]=int(num_reviews_string)
        
        ##Star --> convert text to number
        stars_string = adapter.get("star")
        split_stars_array=stars_string.split(' ')
        stars_text_value=split_stars_array[1].lower()
        if stars_text_value == "zero":
            adapter["star"]= 0
        elif stars_text_value == "one":
            adapter["star"]= 1
        elif stars_text_value == "two":
            adapter["star"]= 2
        elif stars_text_value == "three":
            adapter["star"]= 3
        elif stars_text_value == "four":
            adapter["star"]= 4
        elif stars_text_value == "five":
            adapter["star"]= 5
        
        
        
        return item
