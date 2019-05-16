import unittest
from pyarxaas.arxaas_connector import ARXaaSConnector


class AaaSConnectorTest(unittest.TestCase):

    def setUp(self):
        self.test_data = {
   "data": "age, gender, zipcode\n34, male, 81667\n35, female, 81668\n36, male, 81669\n37, female, 81670\n38, male, 81671\n39, female, 81672\n40, male, 81673\n41, female, 81674\n42, male, 81675\n43, female, 81676\n44, male, 81677",
   "metaData": {
       "sensitivityList":{"age":"IDENTIFYING",
                           "gender":"INSENSITIVE",
                           "zipcode":"INSENSITIVE"
       },
       "dataType": None,
       "hierarchy": {"zipcode":
[["81667", "8166*", "816**", "81***", "8****", "*****"],
["81668", "8166*", "816**", "81***", "8****", "*****"],
["81669", "8166*", "816**", "81***", "8****", "*****"],
["81670", "8167*", "816**", "81***", "8****", "*****"],
["81671", "8167*", "816**", "81***", "8****", "*****"],
["81672", "8167*", "816**", "81***", "8****", "*****"],
["81673", "8167*", "816**", "81***", "8****", "*****"],
["81674", "8167*", "816**", "81***", "8****", "*****"],
["81675", "8167*", "816**", "81***", "8****", "*****"],
["81676", "8167*", "816**", "81***", "8****", "*****"],
["81677", "8167*", "816**", "81***", "8****", "*****"]]},
       "models": {"KANONYMITY":{ "k": "4"}
       }
   }
}

    def test_anonymize_data__run(self):
        pass

