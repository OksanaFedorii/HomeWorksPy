import csv
import uuid


def categories_count_func():
    categories_count = dict()
    for device in categories:
        device_count = len(categories[device])
        categories_count[device] = device_count
    return len(categories_count)


def brand_count_func():
    brand_count = dict()
    for name in brands:
        name_count = len(brands[name])
        brand_count[name] = name_count
    return len(brand_count)


def get_item_by_id(some_id, index_list):
    for some_item in index_list:
        if some_id == some_item[0]:
            return some_item


def print_items_by_category_and_brand():
    # виводить на екран перелік повної інформації про кожний товар одного обраного бренда та однієї обраної категорії
    while True:
        chosen_brand = input("Введіть назву бренду: ")
        chosen_category = input("Введіть категорію: ")

        cat_brand_list = list()
        for some_item in uuid_index:
            if chosen_brand == some_item[1][2] and chosen_category == some_item[1][1]:
                cat_brand_list.append(some_item)
        if len(cat_brand_list) != 0:
            for some_item in cat_brand_list:
                print("ID:", some_item[0])
                print("Назва:", some_item[1][0])
                print("Категорія:", some_item[1][1])
                print("Бренд:", some_item[1][2])
                print("Ціна:", some_item[1][3])
                print("---------------------------")
        else:
            print("На жаль назви даного бренду не знайдено, спробуйте ввести інший бренд")


def create_index_list_from_file(filename):
    with open(filename, mode='r') as csv_file:
        products = csv.reader(csv_file)
        next(products)
        # print(type(reader_1), reader_1)
        index_list = list()
        for row in products:
            indexed_row = (str(uuid.uuid4()), row)
            index_list.append(indexed_row)
            # print(row)
        # print(uuid_index)
        return index_list


def by_categories_and_brands(index_list):
    categories_dict = dict()
    brands_dict = dict()
    for row in index_list:
        if row[1][1] not in categories_dict:
            categories_dict[row[1][1]] = list()
        categories_dict[row[1][1]].append(row[0])
        if row[1][2] not in brands_dict:
            brands_dict[row[1][2]] = list()
        brands_dict[row[1][2]].append(row[0])
    return categories_dict, brands_dict


def count_by_category_and_brands(categories_dict, index_list):
    category_count_by_brand = dict()
    for device in categories_dict:
        items = list()
        for item_id in categories_dict[device]:
            items.append(get_item_by_id(some_id=item_id, index_list=index_list))
        brand_count = dict()
        for item in items:
            if item[1][2] not in brand_count:
                brand_count[item[1][2]] = 0
            brand_count[item[1][2]] = brand_count[item[1][2]] + 1
        category_count_by_brand[device] = brand_count
    return category_count_by_brand


def pretty_print_count_dict(count_dict):
    for cat in count_dict:
        brands_in_dict = count_dict[cat]
        response_str = "В категорії " + cat + " наявні такі бренди з кількістю продукції: "
        for brand in brands_in_dict:
            response_str = response_str + brand + ":" + str(brands_in_dict[brand]) + " "
        print(response_str)


if __name__ == '__main__':
    uuid_index = create_index_list_from_file("tech_inventory.csv")
    categories_and_brands = by_categories_and_brands(uuid_index)

    categories = categories_and_brands[0]
    brands = categories_and_brands[1]

    print("categories: ")
    print(categories)
    print("brands: ")
    print(brands)

    print("Категорій: " + str(categories_count_func()))
    print("Бреднів: " + str(brand_count_func()))

    count_by_category_and_brands = count_by_category_and_brands(categories_dict=categories, index_list=uuid_index)
    pretty_print_count_dict(count_dict=count_by_category_and_brands)

    print_items_by_category_and_brand()
