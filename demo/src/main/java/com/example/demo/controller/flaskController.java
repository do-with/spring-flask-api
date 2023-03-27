package com.example.demo.controller;

import com.example.demo.MyResource;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping("/api")
public class flaskController {
    @GetMapping("/hello")
    public String sayHello() throws JsonProcessingException {
        RestTemplate restTemplate = new RestTemplate();
        String url = "http://localhost:5000/api";
        String text = restTemplate.getForObject(url, String.class);

        ObjectMapper objectMapper = new ObjectMapper();
        ObjectNode objectNode = objectMapper.createObjectNode();
        objectNode.put("text", text);

        return objectMapper.writeValueAsString(objectNode);

    }


}
