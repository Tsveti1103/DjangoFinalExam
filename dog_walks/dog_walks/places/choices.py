from dog_walks.core.mixins import ChoicesEnum

class NightsType(ChoicesEnum):
    HOTEL = 'Хотел'
    GUESTHOUSE = "Вила/Къща за гости"
    HUT = "Хижа"
    BUNGALOW = "Бунгало"
    OTHER = "Други"


class FoodPlacesType(ChoicesEnum):
    RESTAURANT = 'Ресторант'
    PUB = 'Кръчма'
    TAVERN = 'Механа'
    PIZZERIA = 'Пицария'
    FAST_FOOD = 'Бързо хранене'
    OTHER = "Други"


class PriceRange(ChoicesEnum):
    VERY_CHEAP = 'Много евтино'
    CHEAP = 'Евтино'
    NORMALLY = 'Нормално'
    EXPENSIVE = 'Скъпо'
    VERY_EXPENSIVE = 'Много скъпо'


class WalkType(ChoicesEnum):
    WATERFALL = 'Водопад'
    CAVE = 'Пещера'
    DAM = 'Язовир'
    LANDMARKS = 'Природнa забележителност'
    MONASTERY = 'Манастир'
    MONUMENT = 'Паметник'
    MUSEUM = 'Музей'
    ECO_TRAIL = 'Екопътека'
    PARK = 'Парк'
    OTHER = "Други"


class WelcomeDog(ChoicesEnum):
    YES = 'Кучетата са добре дошли'
    MAYBE = 'Позволено с уловие'
    NO = 'Забранено за кучета'


class Difficulty(ChoicesEnum):
    HASSLE_FREE = 'Безпроблемно'
    VERY_EASY = 'Много лесно'
    EASY = 'Лесно'
    AVERAGE = 'Средно'
    HARD = 'Трудно'
    VERY_HARD = 'Много трудно'
    EXTREME = 'Екстремно'


class District(ChoicesEnum):
    BLAGOEVGRAD = 'Благоевград'
    BURGAS = 'Бургас'
    VARNA = 'Варна'
    VELIKOTARNOVO = 'Велико Търново'
    VIDIN = 'Видин'
    VRATSA = 'Враца'
    GABROVO = 'Габрово'
    DOBRICH = 'Добрич'
    KYRDJALI = 'Кърджали'
    KYUSTENDIL = 'Кюстендил'
    LOVECH = 'Ловеч'
    MONTANA = 'Монтана'
    PAZARDZHIK = 'Пазарджик'
    PERNIK = 'Перник'
    PLEVEN = 'Плевен'
    PLOVDIV = 'Пловдив'
    RAZGRAD = 'Разград'
    RUSE = 'Русе'
    SILISTRA = 'Силистра'
    SLIVEN = 'Сливен'
    SMOLYAN = 'Смолян'
    SOFIADISTRICT = 'Софийска област'
    SOFIA = 'София'
    STARAZAGORA = 'Стара Загора'
    TARGOVISHTE = 'Търговище'
    HASKOVO = 'Хасково'
    SHUMEN = 'Шумен'
    YAMBOL = 'Ямбол'


