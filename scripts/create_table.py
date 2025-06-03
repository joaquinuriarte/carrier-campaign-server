import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Get the DATABASE_URL from environment variables
DATABASE_URL = os.environ.get('DATABASE_URL')

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a base class for the models
Base = declarative_base()

# Define the CallData model
class CallData(Base):
    __tablename__ = 'call_data'

    id = Column(Integer, primary_key=True, index=True)
    call_date = Column(DateTime, nullable=True)
    base_price = Column(Float, nullable=True)
    final_price = Column(Float, nullable=True)
    load_origin = Column(String(100), nullable=True)
    call_outcome = Column(String(50), nullable=True)
    call_duration = Column(Integer, nullable=True)  # Duration in seconds
    is_negotiated = Column(Boolean, nullable=True)
    load_destination = Column(String(100), nullable=True)
    carrier_sentiment = Column(String(50), nullable=True)

# Create the table
if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    print("Table 'call_data' created successfully.") 