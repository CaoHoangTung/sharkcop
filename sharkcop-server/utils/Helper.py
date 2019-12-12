import threading
from utils.Checker import Checker

class Helper():
    def url_is_internal(url,compare):
        # url is the param needed to be compared to compare
        if ".".join(extract(url)) == ".".join(extract(compare)) or (url[0:4] != "http" and url[0] != "#"):
            return True
        else:
            return False
            
    def embed_url(url):
        features_size = 30
        threads = [None]*features_size
        arr_threads_result = []
        arr = []
        try:
            threads[0] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.having_IP_Address(arg1),0)), args=(url,))
            threads[1] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.URL_Length(arg1),1)), args=(url,))
            threads[2] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Shortining_Service(arg1),2)), args=(url,))
            threads[3] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.having_At_Symbol(arg1),3)), args=(url,))
            threads[4] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.double_slash_redirecting(arg1),4)), args=(url,))
            threads[5] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Prefix_Suffix(arg1),5)), args=(url,))
            threads[6] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.having_Sub_Domain(arg1),6)), args=(url,))
            threads[7] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.SSLfinal_State(arg1),7)), args=(url,))
            threads[8] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Domain_registeration_length(arg1),8)), args=(url,))
            threads[9] = threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Favicon(arg1),9)), args=(url,))
            threads[10]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.port(arg1),10)), args=(url,))
            threads[11]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.HTTPS_token(arg1),11)), args=(url,))
            threads[12]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Request_URL(arg1),12)), args=(url,))
            threads[13]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.URL_of_Anchor(arg1),13)), args=(url,))
            threads[14]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Links_in_tags(arg1),14)), args=(url,))
            threads[15]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.SFH(arg1),15)), args=(url,))
            threads[16]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Submitting_to_email(arg1),16)), args=(url,))
            threads[17]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Abnormal_URL(arg1),17)), args=(url,))
            threads[18]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Redirect(arg1),18)), args=(url,))
            threads[19]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.on_mouseover (arg1),19)), args=(url,))
            threads[20]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.RightClick (arg1),20)), args=(url,))
            threads[21]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.popUpWidnow (arg1),21)), args=(url,))
            threads[22]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Iframe(arg1),22)), args=(url,))
            threads[23]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.age_of_domain(arg1),23)), args=(url,))
            threads[24]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.DNSRecord(arg1),24)), args=(url,))
            threads[25]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.web_traffic(arg1),25)), args=(url,))
            threads[26]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Page_Rank(arg1),26)), args=(url,))
            threads[27]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Google_Index(arg1),27)), args=(url,))
            threads[28]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Links_pointing_to_page(arg1),28)), args=(url,))
            threads[29]= threading.Thread(target=lambda arg1: arr_threads_result.append((Checker.Statistical_report(arg1),29)), args=(url,))

            for i in range(features_size):
                threads[i].start()
            for i in range(features_size):
                threads[i].join()

            arr_threads_result.sort(key=lambda tup: tup[1])
            for elem in arr_threads_result:
                arr.append(elem[0])
            return arr
        except Exception as e:
            return e