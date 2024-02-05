import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # print("Rows with zero passengers: ", data['passenger_count'].isin([0]).sum())
    data = data[data['trip_distance'] > 0.0]
    data = data[data['passenger_count'] > 0]
    
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print("Number of columns in Camel Case: ", data.columns
                    .str.contains('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                    .sum())
    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
            )

    print("Unique values of Vendor_id: ", data['vendor_id'].unique().tolist() )
    
    return data



@test 
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, "there are rides with zero passengers"
    assert output['trip_distance'].isin([0]).sum() == 0.0, "there are trips with zero distance"
    # assert output['vendor_id'].unique().tolist().sort() != [2,1].sort(), "there are not-existing values in vendor's ids"
