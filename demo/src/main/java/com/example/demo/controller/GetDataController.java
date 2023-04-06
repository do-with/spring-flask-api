package com.example.demo.controller;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class GetDataController {
    // api 경로로 들어가면 그냥 Json 데이터 형태 확인 가능
    @GetMapping("/api")
    public static JSONArray getData() throws Exception {
        RestTemplate restTemplate = new RestTemplate();
        String json = restTemplate.getForObject("http://localhost:5000/img", String.class);
        JSONParser jsonParser = new JSONParser();
        JSONObject jsonObject = (JSONObject) jsonParser.parse(json);
        //JSONObject jsonResponse = (JSONObject) jsonObject.get("title");
        JSONArray jsonTitle = (JSONArray) jsonObject.get("News");
        System.out.print(jsonTitle); // json 문자열
        return jsonTitle;
    }

}