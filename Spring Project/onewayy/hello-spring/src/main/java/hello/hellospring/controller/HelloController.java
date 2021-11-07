package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {

    @GetMapping("hello")   // localhost:8080/hello 를 입력받으면 아래 method 실행
    public String hello(Model model) {
        //spring이 model을 만들어서 넣어주면 그안에 data:hello값을 넣고 return hello에 넘겨줌
        model.addAttribute("data", "hello");
        return "hello"; // resources:templates/hello.html 렌더링
    }
}
