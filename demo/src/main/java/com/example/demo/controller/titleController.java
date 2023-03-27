package com.example.demo.controller;

import org.springframework.ui.Model;
import com.example.demo.MyResource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/api")
public class titleController {

    @GetMapping(value = "/view")
    public String getView(Model model) throws Exception {
        model.addAttribute("Data", MyController.getData());
        return "view";
    }
}