import colour # pip install colour-science
# https://pypi.org/project/colour-science/#colour-appearance-models-colour-appearance
# https://colour.readthedocs.io/en/latest/generated/colour.models.eotf_ST2084.html
import numpy as np

def calculate_hdr_deltaITP(img1, img2):
    img1 = img1[:, :, [2, 1, 0]]
    img2 = img2[:, :, [2, 1, 0]]
    img1 = img1/255;
    img2 = img2/255;
    # 按照BT2100，在计算eotf之前，应该先把输入归一化到[0,1]。所以此代码需要修改。
    img1 = colour.models.eotf_ST2084(img1) #已验证。与BT2100表4的PQ-EOTF计算出来的值完全一致。fanld
    img2 = colour.models.eotf_ST2084(img2)
    # get linear rgb, afterwards, convert linear rgb to ICTCP according ICTCP dolby white paper.
    img1_ictcp = colour.RGB_to_ICTCP(img1)
    img2_ictcp = colour.RGB_to_ICTCP(img2)
    # ref: BT.2124
    delta_ITP = 720 * np.sqrt((img1_ictcp[:,:,0] - img2_ictcp[:,:,0]) ** 2
                            + 0.25 * ((img1_ictcp[:,:,1] - img2_ictcp[:,:,1]) ** 2)
                            + (img1_ictcp[:,:,2] - img2_ictcp[:,:,2]) ** 2)
    return np.mean(delta_ITP)
    