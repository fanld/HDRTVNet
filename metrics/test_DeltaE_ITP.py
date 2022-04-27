import cv2
import metrics.DeltaE_ITP

im1 = cv2.imread('/tmp/HDRTVNET_ubuntu/dataset/dataset/test_set/test_hdr/001.png');
im2 = cv2.imread('/tmp/HDRTVNET_ubuntu/dataset/dataset/test_set/test_hdr/002.png');

out = metrics.DeltaE_ITP.calculate_hdr_deltaITP(im1, im2)

print(out)
