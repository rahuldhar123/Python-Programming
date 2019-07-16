import pandas as pd
prediction = pd.DataFrame()
imageid = []
for i in range(len(X_test)):
    i = i + 1
    imageid.append(i)
prediction["ImageId"] = imageid
prediction["Label"] = model.predict_classes(X_test, verbose=0)
print(prediction.head())

import numpy as np
a  = np.array(y_test[0:5])
print('Actual labels for first five images: {0}'.format(np.argmax(a, axis=1)))