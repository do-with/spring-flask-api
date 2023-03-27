package com.example.demo.controller;

import ch.qos.logback.core.model.Model;
import com.example.demo.MyResource;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
public class MyController {

    @GetMapping("/api")
    public static MyResource getData() throws Exception {
        RestTemplate restTemplate = new RestTemplate();
        String json = restTemplate.getForObject("http://localhost:5000/api", String.class);
        ObjectMapper objectMapper = new ObjectMapper();
        Map<String, Object> map = objectMapper.readValue(json, Map.class);
        MyResource myData = new MyResource();
        myData.setId((Integer) map.get("id"));
        myData.setTitle((String) map.get("title"));
        System.out.print(myData.getId());
        return myData;
    }

}