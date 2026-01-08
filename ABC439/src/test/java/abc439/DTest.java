package abc439;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

class DTest {

    private static String stripLastNewline(String s) {
        // 末尾の改行だけを1個除去（\n / \r\n 対応）
        return s.replaceFirst("\\R\\z", "");
    }

    private static String show(String s) {
        // 見比べやすい表示（改行を可視化）
        return s.replace("\r", "\\\\r").replace("\n", "⏎\\n");
    }


    @Test
    void sample1() {
        String input = "10\r\n3 10 7 10 7 6 7 6 5 14";
        String expected = "7";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            D.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample2() {
        String input = "6\r\n210 210 210 210 210 210";
        String expected = "0";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            D.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample3() {
        String input = "21\r\n49 30 50 21 35 15 21 70 35 9 50 70 21 49 30 50 70 15 9 21 30";
        String expected = "34";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            D.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


}
