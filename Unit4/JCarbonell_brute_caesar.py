from JCarbonell_caesar import decrypt

def brute_decrypt(message):
    for key in range(26):
        print (decrypt(key,message))
        
message = "PMTTW NZWU BPM XIAB! BPMZM QA VWBPQVO BW AMM PMZM. EMTKWUM BW BPM EWZTL WN KZGXBWOZIXPG. BWBITTG NCV ABCNN!"

brute_decrypt(message)
        