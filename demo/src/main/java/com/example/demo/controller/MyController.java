package com.example.demo.controller;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class MyController {

    @GetMapping("/api")
    public static JSONArray getData() throws Exception {
        RestTemplate restTemplate = new RestTemplate();
        String json = restTemplate.getForObject("http://localhost:5000/notice", String.class);
        JSONParser jsonParser = new JSONParser();
        JSONObject jsonObject = (JSONObject) jsonParser.parse(json);
        //JSONObject jsonResponse = (JSONObject) jsonObject.get("title");
        JSONArray jsonTitle = (JSONArray) jsonObject.get("t");
        System.out.print(jsonTitle); // json 문자열

        //ObjectMapper objectMapper = new ObjectMapper();
        //MyResource myData = new MyResource();
        //JSONObject rjson = new JSONObject(json);
        //for(int i = 0; i < jsonTitle.size(); i++){
            //JSONObject item = (JSONObject) jsonTitle.get(i);
            //JSONObject item = (JSONObject) jsonTitle.get(i);

            //System.out.print(item);

            //Map<String, Object> map = objectMapper.readValue(item, Map.class);
            //myData.setId((Integer) Integer.parseInt(String.valueOf(item.get("id"))));
            //myData.setTitle((String) item.get("title"));
            //System.out.print(myData.getId());
        //}
        return jsonTitle;
    }

}