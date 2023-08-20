from glob import glob

train_img_list = glob('C:\\Users\\admin\\Desktop\\wooil\\Hyper\\2D_Bounding_Box\\2D Bounding Box\\training\\images\\*.jpg')
valid_img_list = glob('C:\\Users\\admin\\Desktop\\wooil\\Hyper\\2D_Bounding_Box\\2D Bounding Box\\validation\\images\\*.jpg')

# 리스트를 txt파일로 생성
with open('C:\\Users\\admin\\Desktop\\wooil\\Hyper\\2D_Bounding_Box\\2D Bounding Box\\train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')

with open('C:\\Users\\admin\\Desktop\\wooil\\Hyper\\2D_Bounding_Box\\2D Bounding Box\\valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')