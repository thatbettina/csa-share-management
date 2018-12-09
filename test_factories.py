import datetime
import factory

from solawi.app import db
from solawi.models import Station, Share, Bet, Person, Member


class StationFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Station
        sqlalchemy_session = db.session   # the SQLAlchemy session object
        sqlalchemy_session_persistence = 'commit'

    name = factory.Sequence(lambda n: u'Station %d' % n)


class ShareFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Share
        sqlalchemy_session = db.session   # the SQLAlchemy session object
        sqlalchemy_session_persistence = 'commit'

    station = factory.SubFactory(StationFactory)


class BetFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Bet
        sqlalchemy_session = db.session   # the SQLAlchemy session object
        sqlalchemy_session_persistence = 'commit'

    start_date = datetime.date(2018, 1, 1)
    end_date = None
    share = factory.SubFactory(ShareFactory)
    value = 90


class PersonFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Person
        sqlalchemy_session = db.session   # the SQLAlchemy session object
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('full_name')
    share = factory.SubFactory(ShareFactory)

class MemberFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Member
        sqlalchemy_session = db.session   # the SQLAlchemy session object
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('name')
    phone = factory.Faker('phone_number')
    email = factory.Faker('safe_email')
    share = factory.SubFactory(ShareFactory)