curl -XGET "http://172.16.203.19:9200/winlogbeat-6.2.4-*/_search" -H 'Content-Type: application/json' -d'
{
  "aggs": {
    "2": {
      "terms": {
        "field": "beat.name",
        "size": 100,
        "order": {
          "_count": "desc"
        }
      },
      "aggs": {
        "3": {
          "terms": {
            "field": "event_data.TargetUserName",
            "size": 100,
            "order": {
              "_count": "desc"
            }
          },
          "aggs": {
            "4": {
              "terms": {
                "field": "event_data.WorkstationName",
                "size": 100,
                "order": {
                  "_count": "desc"
                }
              },
              "aggs": {
                "5": {
                  "terms": {
                    "field": "event_data.IpAddress",
                    "size": 100,
                    "order": {
                      "_count": "desc"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "size": 0,
  "version": true,
  "_source": {
    "excludes": []
  },
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [
    {
      "field": "@timestamp",
      "format": "date_time"
    }
  ],
  "query": {
    "bool": {
      "must": [
        {
          "match_all": {}
        },
        {
          "match_all": {}
        },
        {
          "query_string": {
            "query": "event_data.TargetUserName: Administrator || administrator",
            "analyze_wildcard": true,
            "default_field": "*"
          }
        },
        {
          "range": {
            "@timestamp": {
              "from": "now-24h",
              "format": "epoch_millis"
            }
          }
        },
        {
          "match_phrase": {
            "event_data.LogonType": {
              "query": "10"
            }
          }
        }
      ],
      "filter": [],
      "should": [],
      "must_not": []
    }
  },
  "highlight": {
    "pre_tags": [
      "@kibana-highlighted-field@"
    ],
    "post_tags": [
      "@/kibana-highlighted-field@"
    ],
    "fields": {
      "*": {}
    },
    "fragment_size": 2147483647
  }
}' >  /home/gaurav.khe/downloaded_data.json
