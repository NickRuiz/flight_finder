3hk.proxy.novarra.com:
  mode: normal
  port: 8827
  ua_string: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1
  headers:
     Cookie: Novarra-Device-ID=666;SESSIONID=6
     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 
  video_sites:
    - uri: http://youtube.com
      regex: href=\"(\S+\watch\?v=\w+)\"
