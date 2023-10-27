import matplotlib.pyplot as plt

#This is the accuracies of the first 100 epoch 
accuracies = [0.4962, 0.5274, 0.5917, 0.4944, 0.5124, 0.5476, 0.5922, 0.5431, 0.5013, 0.5294, 0.5464, 0.5487, 0.5922, 0.6340, 0.5876, 0.6005, 0.6104, 0.6167, 0.6243, 0.6215, 0.6473, 0.6436, 0.5936, 0.6391, 0.6030, 0.6030, 0.5675, 0.6116, 0.6212, 0.5968, 0.5843, 0.6056, 0.6073, 0.6175, 0.5985, 0.5948, 0.6186, 0.5752, 0.6056, 0.5769, 0.6042, 0.6212, 0.5825, 0.5931, 0.5786, 0.6002, 0.5712, 0.5624, 0.5907, 0.5848, 0.6260, 0.6030, 0.5854, 0.5819, 0.6329, 0.6042, 0.6204, 0.6106, 0.6110, 0.6112, 0.6126, 0.6126, 0.6135, 0.6098, 0.6081, 0.6087, 0.6130, 0.6167, 0.6118, 0.6130, 0.6135, 0.6124, 0.6118, 0.6135, 0.6124, 0.6106, 0.6141, 0.6147, 0.6141, 0.6112, 0.6118, 0.6130, 0.6153, 0.6135, 0.6130, 0.6101, 0.6124, 0.6135, 0.6141, 0.6095, 0.6147, 0.6112, 0.6118, 0.6093, 0.6159, 0.6098, 0.6087, 0.6093, 0.6093, 0.6093]
#This is the loss for the first 100 epoch
loss = [0.6979881910716786, 0.6844412877279169, 0.6904780426446129, 0.684895454084172, 0.6812622880234438, 0.6792347308467416, 0.6771022852729348, 0.6855413440395804, 0.6720500413109275, 0.6870778799057007, 0.6519009260570302, 0.6404731641797459, 0.6227208665188622, 0.5900690169895396, 0.5951909887440064, 0.5607741247205174, 0.5638843687141643, 0.5399825283709694, 0.5193865106386297, 0.4769795151317821, 0.46142111543346853, 0.45512034174273996, 0.4230612568995532, 0.3895933969932444, 0.39457252358689027, 0.3760155246538274, 0.37903575160924124, 0.3169827342909925, 0.3307492321028429, 0.25006428689641114, 0.2171676978468895, 0.284952069468358, 0.19351636508808417, 0.19536656217978282, 0.1634677432696609, 0.11777753673274727, 0.14037292516406844, 0.23939100105096311, 0.11117816716432571, 0.06792027106070343, 0.11127064086715965, 0.08680430388845065, 0.08349954084876705, 0.0602918595815187, 0.04537964773172622, 0.018756276154068902, 0.017304050311555758, 0.0667554905932561, 0.056819359415813404, 0.01601847937426475, 0.0256724186885335, 0.08536267633248559, 0.016678674338275894, 0.021344836472588426, 0.03200960334951935, 0.054271318350562495, 0.032041940687443406, 0.008468315467539737, 0.0025479644400012843, 0.0009727750567596077, 0.0007114587334559902, 0.0006080651262035483, 0.0005404480839120772, 0.0004825884388992563, 0.00043984228036339013, 0.0004121263824773076, 0.00037888841025586077, 0.0003548304273007328, 0.0003334864805390894, 0.0003150697696529438, 0.0002981368049992906, 0.00028354384695001715, 0.00027058320034377496, 0.0002587148782742374, 0.00024809086993199717, 0.00023693855730337366, 0.0002282507754417191, 0.00022031878153725034, 0.00021815271654358024, 0.0002045452338814571, 0.00019706551778226103, 0.00019002843627651388, 0.0001844407169675619, 0.00017817121774629305, 0.00017225533241905985, 0.00016851070519324448, 0.00016327866144231795, 0.0001579179693448275, 0.00015318737795870917, 0.00014883789652444916, 0.00014545178911409013, 0.00014506131992675364, 0.00013773206635104383, 0.00013385336698026068, 0.00013058477484532085, 0.00012730956672492218, 0.00012449162686072455, 0.00012149684548871043, 0.0001185430414539844, 0.00011599305349484305]


epoch = list(range(100))


plt.figure(figsize=(12, 6))
plt.plot(epoch, accuracies, marker='o', linestyle='-', color='b', label='Accuracy')
plt.title('Accuracy vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()



plt.plot(range(len(loss)), loss, marker='o', linestyle='-', color='b', label='Loss')
plt.title('Loss vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()